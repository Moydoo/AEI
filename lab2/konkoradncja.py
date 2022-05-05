from clp3 import clp
from copy import copy
import clp_settings
import os, random
import re
splitters = ['!', '?', ';', '\n']
marks = [ ',','#',':','@','$','%','^','&','*','(',')','<','>','/','-','+','=','–','"','`']


#functions
def find_key_word(sentence, key):
    filtered_sentence = sentence
    for m in marks:
        filtered_sentence = filtered_sentence.replace(m,"")
    splitted_sentence = filtered_sentence.split(" ")
    for s in splitted_sentence:
        word_clp = clp(s)
        if word_clp:
            word_id = word_clp[0]
        else:
            continue
        if word_id == key:
            return True
    return False

key_word = input('Zarzuć wyrazem śq: ')
key_word_id = clp(key_word)[0]


#algorythm
DIR = 'whole'
text_files = os.listdir(DIR)
texts = []
#Wyciąganie tekstów w pętli
for i, t_f in enumerate(text_files):
    with open(DIR + '/' + t_f, "r", encoding = "utf-8") as handle:
        text = handle.read()
        for splitter in splitters:
            text = text.replace(splitter, '.')
        text = text.split('.')
        #w_s index zdania, s - zdanie
        for w_s, s in enumerate(text):
            if find_key_word(s, key_word_id):
                print('Tekst {}, zdanie {}:{}'.format(i + 1, w_s + 1, s))


