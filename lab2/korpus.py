#imports
from clp3 import clp
from copy import copy
import clp_settings
import os, random

#Lists
marks = ['.', ',', '?', '!','#',':','@','$','%','^','&','*','(',')','<','>','/',';','-','+','=','\n','–','"','`']
DIRS = ['whole','ksiazki','nieksiazki']
non_POS = ['E','F','G']
stoplist = ['być','jak','inne','33']

#generating freq dictionary
def generate_freq_dic(text):
    text = text.lower()
    for m in marks:
        text = text.replace(m,"")

    text_list = text.split(" ")
    freq_dic = {}
    for word in text_list:
        if clp(word):
            word_bform = clp.bform(clp(word)[0]).split()[0]
            if word_bform in freq_dic.keys():
                freq_dic[word_bform] += 1
            else:
                freq_dic[word_bform] = 1
    return freq_dic


#changing dictionary to list (tuple)
def get_freq_list(dic):
    return [tuple((k, v, clp.label(clp(k)[0])[0])) for k,v in dic.items()]

#creating POS file
def get_label_dic(f_list):
    label_dic = {}
    for _,_,label in f_list:
        if label in label_dic.keys():
            label_dic[label] += 1
        else:
            label_dic[label] = 1
    label_dic.update((k, tuple((v, v / len(f_list)))) for k, v in label_dic.items())
    return label_dic

for dir in DIRS:
    text_files = os.listdir(dir)
    random.shuffle(text_files)
    texts = []
    freq_list_sorter = lambda x: x[1]
    #Wyciąganie tekstów w pętli
    for t_f in text_files:
        with open(dir + '/' + t_f, "r", encoding = "utf-8") as handle:
            texts.append(handle.read())



    #changing texts to one string
    splitted_text = '\n###\n'.join(texts)
    #freq dictionary
    splitted_freq_dic = generate_freq_dic(splitted_text)
    print(splitted_freq_dic['mieć'])
    print(2/0)
    #freq list
    splitted_freq_list = get_freq_list(splitted_freq_dic)
    #sorted freq list
    sorted_splitted_freq_list = sorted(splitted_freq_list, key = freq_list_sorter, reverse = True)

    #part of speach
    pos = get_label_dic(sorted_splitted_freq_list)
    #removing unnecesssary POS
    filtered_freq_list = list(filter(lambda x: x[2] not in non_POS, sorted_splitted_freq_list))
    #freq_list with stoplist
    stoplist_freq_list = list(filter(lambda x: x[2] not in non_POS and x[0] not in stoplist, sorted_splitted_freq_list))
    #freq_list with hapax (endlist)
    hapax_freq_list = list(filter(lambda x: x[2] not in non_POS and x[0] not in stoplist and x[1] > 1, sorted_splitted_freq_list))

    #creating POS for stoplist and hapax
    pos_stoplist = get_label_dic(copy(stoplist_freq_list))
    pos_hapax = get_label_dic(copy(hapax_freq_list))

    #sorted basic freq_list
    with open('freq_list_' + dir + '.txt', 'w', encoding = 'utf-8') as file:
        file.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in sorted_splitted_freq_list))
    #POS for sorted basic freq_list
    with open('POS_' + dir + '.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join('{} {} {}%'.format(label, pos[label][0], pos[label][1]*100) for label in sorted(pos)))

    #Filtered freq_list (removed unnecessary POS)
    with open('filtered_freq_list_' + dir + '.txt', 'w', encoding = 'utf-8') as file:
        file.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in filtered_freq_list))

    #stoplist freq_list with stoplist
    with open('stoplist_' + dir + '.txt', 'w', encoding = 'utf-8') as file:
        file.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in stoplist_freq_list))

    #Hapax freq_list (endlist)
    with open('hapax_' + dir + '.txt', 'w', encoding = 'utf-8') as file:
        file.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in hapax_freq_list))

    #POSs stoplist+hapax
    with open('POS_stop_' + dir + '.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join('{} {} {}%'.format(label, pos[label][0], pos[label][1]*100) for label in sorted(pos_stoplist)))
    with open('POS_hapax_' + dir + '.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join('{} {} {}%'.format(label, pos[label][0], pos[label][1]*100) for label in sorted(pos_hapax)))

