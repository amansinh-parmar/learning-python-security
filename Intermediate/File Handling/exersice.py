from translate import Translator

translator = Translator(to_lang='ja')
# trasnsition = translator.ts('This is a Apple')
# print(trasnsition)

try:
    with open('practice.txt', mode='r') as translate_file:
        text = translate_file.read()
        # print('\n',text, '\n')
        translation = translator.translate(text)
        print('\n',translation,'\n')
except FileNotFoundError:
    print('This File is NOT FOUND!!')