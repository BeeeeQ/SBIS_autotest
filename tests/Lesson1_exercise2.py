import os
count_py = 0
count_exe = 0
count_folders = 0
list_dir = os.listdir(r'C:\Users\si.kuricyn\AppData\Local\Programs\Python\Python310')
for el in list_dir:
    el = os.path.splitext(el)
    if el[-1] == '.py':
        count_py += 1
    if el[-1] == '.exe':
        count_exe += 1
    if el[-1] == '':
        count_folders += 1
count_files = len(list_dir) - count_folders

my_file = open("../Dir_count.txt", "w+")
my_file.write(f"Папок: {count_folders}\n")
my_file.write(f"Файлов с расширением '.py': {count_py}\n")
my_file.write(f"Файлов с расширением '.exe': {count_exe}\n")
my_file.write(f"Всего файлов: {count_files}\n")
my_file.close()
