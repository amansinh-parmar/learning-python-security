# ==> Simple way to Translate the Text
# from translate import Translator

# translator = Translator(to_lang='hi')
# # trasnsition = translator.ts('This is a Apple')
# # print(trasnsition)

# try:
#     with open('practice.txt', mode='r') as translate_file:
#         text = translate_file.read()
#         # print('\n',text, '\n')
#         translation = translator.translate(text)
#         print('\n',translation,'\n')
# except FileNotFoundError:
#     print('This File is NOT FOUND!!')


# ==> Simple way to Translate the Text and Save it in a New File.
from translate import Translator

translator = Translator(to_lang='fr')
try:
    with open('practice.txt', mode='r', encoding='utf-8') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # print(translation)
        with open('translate_file.txt', mode='w', encoding='utf-8') as new_file:
            new_file.write(translation)
except FileNotFoundError as err:
    print('Soerry, This file is NOT FOUND!!')
    # raise err
