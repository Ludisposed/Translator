# -*- coding: utf-8 -*-
from googletrans import Translator
import os
translator = Translator()
FILENAME = 'translations.txt'

def translate_string(inp):
    translated_part = translator.translate(inp, dest='zh-CN')
    if os.path.exists(FILENAME):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    try:
        f = open(FILENAME,append_write)
        f.write('Origin: %s\n' % (translated_part.origin.encode('utf-8')))
        f.write('Translation: %s\n\n' % (translated_part.text.encode('utf-8')))
        f.close()
        
    except Exception, e:
        print e
        f.close()

if __name__ == "__main__":
    inp = raw_input('What do you want to translate: ')
    translate_string(inp)
