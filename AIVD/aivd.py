from googletrans import Translator
import sys

def readfile(filename):
    words = []
    with open(filename,'r') as f:
        for line in f:
            words += line.split(' ')

    return [w.lower() for w in words]

def writefile(filename, text, vocabularies):
    with open(filename, 'a') as f:
        f.write('\n\n')
        f.write(text)
        f.write('\n\n')
        f.write(vocabularies)

def translate(words):
    translator = Translator(service_urls=['translate.google.cn'])
    text = ""
    vocabularies_s = set()
    vocabularies_d = set()
    for word in words:
        word = word.strip('.!,:;?*\n')
        translated_part = translator.translate(word, dest = 'en', src = 'nl')
        text += translated_part.text + ' '
        if word.isalpha():
            if word == translated_part.text:
                vocabularies_s.add(word + ' : ' + translated_part.text)
            else:
                vocabularies_d.add(word + ' : ' + translated_part.text)
    return text, '\n'.join(sorted(list(vocabularies_s)) + [' '] + sorted(list(vocabularies_d)))

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if 10 <= int(sys.argv[1]) <= 41:
            filename = 'opgaves/{}.txt'.format(sys.argv[1])
        elif 0 <= int(sys.argv[1]) < 10:
            filename = 'opgaves/0{}.txt'.format(sys.argv[1])
        else:
            filename = 'opgaves/00.txt'
    else:
        filename = 'opgaves/00.txt'
    words = readfile(filename)
    text, vocabularies = translate(words)
    writefile(filename, text, vocabularies)

   


