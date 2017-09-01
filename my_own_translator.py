# -*- coding: utf-8 -*-
import googletrans
from googletrans import Translator
import sys
import os

LANGCODES = dict(map(reversed, googletrans.LANGUAGES.items()))
class MyTranslator(object):

    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.cn'])
        self.filename = 'translations.txt'

    def translate_chinese_to_english(self, inp):
        self.translate_string(inp, 'en', 'zh-CN')
    def translate_english_to_chinese(self, inp):
        self.translate_string(inp, 'zh-CN','en')

    def translate_string(self, inp, dest='en', src = 'auto'):
        dest = self.dest_language(dest)
        if src != 'auto':
            src = self.dest_language(src)
        print(dest, src)
        translated_part = self.translator.translate(inp, dest = dest, src = src)
        origin = translated_part.origin.encode('utf-8')
        text = translated_part.text.encode('utf-8')
        print('*** Translated: '+ text)

        self.save_text(origin, src + '.txt')
        self.save_text(text, dest + '.txt')
    def save_text(self, text, filename):
        if os.path.exists(filename):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        try:
            f = open(filename,append_write)
            f.write(' ' + text)
            f.close()

        except Exception as e:
            print(e)
            f.close()
    def dest_language(self, language):
        if language in googletrans.LANGUAGES:
            return language
        language = language.lower()
        d = self.translator.detect(language).lang
        if d == 'en' and language != 'english':
            if language == 'chinese':
                return 'zh-CN'
            return LANGCODES[language]
        return d

def textfile_2_text(textfile):
    text = ''
    if os.path.isfile(textfile) and os.path.exists(textfile):
        with open(textfile, 'r') as f:
            text = ' '.join([i for i in f])
    return text

if __name__ == "__main__":
    transtor = MyTranslator()
    inp = ''
    if len(sys.argv[2]) > 0:
        inp = textfile_2_text(sys.argv[2])
    else:
        inp = raw_input('*** What do you want to translate: ')
    
    if len(sys.argv[1]) > 0:
        if sys.argv[1] == '1':
            transtor.translate_english_to_chinese(inp)
        elif sys.argv[1] == '2':
            transtor.translate_chinese_to_english(inp)
    else:
        dest = raw_input('*** Which language do you want to translated to: ')
        transtor.translate_string(inp,dest)



