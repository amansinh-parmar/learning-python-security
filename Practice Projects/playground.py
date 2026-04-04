# from practice import Person

# per = Person()
# # print(per.usr_name())
# print(per.usr_age())
# # per()

import os 

rename_file = os.listdir(r"D:\PyCharm\mergePDF")
i = 'A'
for file in rename_file:
    if file.endswith(".pdf"):
        os.rename(f"D:\PyCharm\mergePDF\{file}", f"D:\PyCharm\mergePDF\{i}.pdf")
        i = i + 'A'
        print(file)

# if file:
#     os.remove(r"D:\PyCharm\mergePDF\A")
#     print(file)

file_name = [r'A.pdf', r'AA.pdf']
with open("D:\PyCharm\mergePDF", 'w') as outfile:
    for fnmae in file_name:
        with open(fnmae) as infile:
            for line in infile:
                outfile.write(line)