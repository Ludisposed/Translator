# -*- coding: utf-8 -*-
import googletrans
from googletrans import Translator

import os
FILENAME = 'translations.txt'
LANGCODES = dict(map(reversed, googletrans.LANGUAGES.items()))
class MyTranslator(object):

    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.cn'])
        self.filename = 'translations.txt'

    def translate_chinese_to_english(self, inp):
        translate_string(self,inp, dest = 'en', src='zh-cn')
    def translate_english_to_chinese(self, inp):
        translate_string(self, inp, dest='zh-cn',src='en')

    def translate_string(self, inp, dest='en', src = 'auto'):
        dest = self.dest_language(dest)
        if src != 'auto':
            src = self.dest_language(dest)
        translated_part = self.translator.translate(inp, dest = dest, src = src)
        origin = translated_part.origin.encode('utf-8')
        text = translated_part.text.encode('utf-8')
        print('*** Translated: '+text)
        if os.path.exists(FILENAME):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        try:
            f = open(self.filename,append_write)
            f.write('Origin: %s\n' % (origin))
            f.write('Translation: %s\n\n' % (text))
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




if __name__ == "__main__":
    transtor = MyTranslator()
    dest = raw_input('*** Which language do you want to translated to: ')
    inp = raw_input('*** What do you want to translate: ')
    transtor.translate_string(inp,dest)
