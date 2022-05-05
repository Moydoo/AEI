from clp3 import clp
import os
import codecs
TEXTS_DIR = "texts"
removal_marks = ['!', '?', ';', '\n', '.', ',','#',':','@','$','%','^','&','*','(',')','<','>','/','-','+','=','–','"','`']


class TextInfo:

    def __init__(self, text, target_map: dict):
        self._text = text
        self._target_map = target_map
        self._targets, self._accuracy = self.get_text_target_info()

    def get_text_info(self):
        return {
            "text": self._text,
            "accuracy": self._accuracy,
            "target_words": self._targets
        }

    def get_text_target_info(self):
        clear_text = self._text.lower()
        for m in removal_marks:
            clear_text = clear_text.replace(m, '')
        splitted_text = clear_text.split(' ')
        bform_splitted_text = []
        for word in splitted_text:
            if clp(word):
                word_bform = clp.bform(clp(word)[0]).split()[0]
                bform_splitted_text.append(word_bform)
            else:
                bform_splitted_text.append(word)
        attendance = {}
        for (target_word, items) in self._target_map.items():
            attend_words = [i for i in items[0] if i in bform_splitted_text]
            if attend_words:
                attendance[target_word] = tuple((attend_words, items[1]))
        new_attendance = {}
        accuracy = 0
        for name, values in attendance.items():
            new_attendance[name] = values[0]
            accuracy += values[1]
        return new_attendance, accuracy


def get_raw_text_info(text_name, t_map):
    with codecs.open("texts/" + text_name, 'r', encoding="utf-8", errors="ignore") as f:
        t = f.read()
    ti = TextInfo(t, t_map)
    return ti.get_text_info()


def get_all_text_info(targets_map):
    files = os.listdir("texts")
    infos = {}
    for file in files:
        infos[file[:-4]] = get_raw_text_info(file, targets_map)

    return infos
