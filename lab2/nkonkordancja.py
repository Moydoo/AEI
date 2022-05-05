from clp3 import clp
from copy import copy
import clp_settings
import os, random
import re
splitters = ['!', '?', ';', '\n']
marks = [ ',','#',':','@','$','%','^','&','*','(',')','<','>','/','-','+','=','–','"','`']


# functions
def find_key_word(sentence, key):
    filtered_sentence = sentence
    for m in marks:
        # grooming from unnecessary marks
        filtered_sentence = filtered_sentence.replace(m, "")
    splitted_sentence = filtered_sentence.split(" ")
    for ix, sx in enumerate(splitted_sentence):
        word_clp = clp(sx)
        if word_clp:
            word_id = word_clp[0]
        else:
            continue
        if word_id == key:
            return True, ix
    return False, -1

key_word = input('Zarzuć wyrazem: ')
#clp bform
key_word_id = clp(key_word)[0]
#algorythm
DIR = 'whole'
text_files = os.listdir(DIR)
texts = []

#loop for picking texts
for i, t_f in enumerate(text_files):
    with open(DIR + '/' + t_f, "r", encoding = "utf-8") as handle:
        text = handle.read()
        for splitter in splitters:
            text = text.replace(splitter, '.')
        text = text.split('.')
        #w_s index zdania, s - zdanie
        for w_s, s in enumerate(text):
            if not s:
                continue
            if s[0] == " ":
                s = s[1:]
            result = find_key_word(s, key_word_id)
            if result[0]:
                splitted_s = s.split(' ')
                bottom_index = 0 if result[1] - 4 < 0 else result[1] - 4
                top_index = min(result[1]+5, len(splitted_s))
                splitted_sentence_to_print = list(filter(lambda word: word, splitted_s))
                print('Tekst {}: {}'.format(i + 1, ' '.join(splitted_sentence_to_print[bottom_index:top_index])))


