# imports
from clp3 import clp
from copy import copy
import clp_settings
import os, random
import itertools
from collections import Counter
import math
import pandas as pd

# Lists
marks = ['.', ',', '?', '!', '#', ':', '@', '$', '%', '^', '&', '*', '(', ')', '<', '>', '/', ';', '-', '+', '=', '\n',
         '–', '"', '`']
DIRS = ['whole']
Win = 5


# generating freq dictionary
def generate_freq_dic(text_list):
    freq_dic = {}
    for word in text_list:
        if clp(word):
            word_to_dict = clp.bform(clp(word)[0]).split()[0]
        else:
            word_to_dict = word
        if word_to_dict in freq_dic.keys():
            freq_dic[word_to_dict] += 1
        else:
            freq_dic[word_to_dict] = 1
    return freq_dic


def get_par_probability(text_list):
    pair_probability_dict = {}
    # Pierwsze wyrażenie to ilośc kombinacji par o długości Win * ilość okien o długości Win w całym tekście
    pair_all_amount = len(list(itertools.combinations(range(Win), 2))) * (len(text_list) - Win + 1)
    num = 0
    pair_dict = {}
    for i in range(len(text_list) - Win + 1):
        window_words = text_list[i: i + Win]
        clp_window_words = []
        for w in window_words:
            if clp(w):
                clp_window_words.append(clp.bform(clp(w)[0]).split()[0])
            else:
                clp_window_words.append(w)
        win_freq_pair_dict = win_pair_appearances(clp_window_words)
        for pair, amount in win_freq_pair_dict.items():
            pair_dict[pair] = pair_dict.get(pair, 0) + amount
    pair_dict.update({(k, (v, v / pair_all_amount)) for k, v in pair_dict.items()})
    return pair_dict


def win_pair_appearances(window):
    combined_win_pairs = itertools.combinations(window, 2)
    return dict(Counter(combined_win_pairs))


# changing dictionary to list (tuple)
def get_freq_list(dic):
    return [tuple((k, v, clp.label(clp(k)[0])[0])) for k, v in dic.items()]


def get_freq_pair_dict(text_list):
    freq_pair_dic = {}
    for i in range(len(text_list) - 1):
        f, s = text_list[i: i + 2]
        if clp(f) and clp(s):
            f_bform, s_bform = get_word_bform(f), get_word_bform(s)
            freq_pair_dic[(f_bform, s_bform)] = freq_pair_dic.get((f_bform, s_bform), 0) + 1
    return freq_pair_dic


def get_word_bform(word):
    return clp.bform(clp(word)[0]).split()[0]


for dir in DIRS:
    text_files = os.listdir(dir)
    random.shuffle(text_files)
    texts = []
    freq_list_sorter = lambda x: x[1]
    # Wyciąganie tekstów w pętli
    for t_f in text_files:
        with open(dir + '/' + t_f, "r", encoding="utf-8") as handle:
            texts.append(handle.read())

    # changing texts to one string
    splitted_text = '\n ###\n'.join(texts)
    splitted_text_lower = splitted_text.lower()
    for m in marks:
        splitted_text_lower = splitted_text_lower.replace(m, " ")
    splitted_text_list = splitted_text_lower.split()
    # freq dictionary
    splitted_freq_dic = generate_freq_dic(splitted_text_list)
    # freq_pair_dics
    pair_probability_dict = get_par_probability(splitted_text_list)
    # print(pair_probability_dict)
    words_amount = len(splitted_text_list)
    pair_pmi = {}
    df = pd.DataFrame(columns=["f_word", "s_word", "f_amount", "s_amount", "pair_amount", "pmi"])
    for pair, probs in pair_probability_dict.items():
        amount, probability = probs
        f_prob = splitted_freq_dic[pair[0]] / words_amount
        s_prob = splitted_freq_dic[pair[1]] / words_amount
        # log (probability/ (f_prob * s_prob))
        probability_value = probability / (f_prob * s_prob)

        if probability_value:
            pair_pmi[pair] = math.log(probability_value,2)
            df = df.append({"f_word": pair[0], "s_word": pair[1], "f_amount": splitted_freq_dic[pair[0]],
                            "s_amount": splitted_freq_dic[pair[1]], "pair_amount": amount, "pmi": math.log(probability_value,2)}, ignore_index=True)
        else:
            pair_pmi[pair] = 0
            df = df.append({"f_word": pair[0], "s_word": pair[1], "f_amount": splitted_freq_dic[pair[0]],
                            "s_amount": splitted_freq_dic[pair[1]], "pair_amount": amount, "pmi": 0}, ignore_index = True)
    df = df.sort_values("pmi", ascending=False)
    print(df.head())
    df.to_csv("ksiazki_prob.csv", index=False)