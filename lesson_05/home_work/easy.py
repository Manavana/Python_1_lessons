__author__ = "Стиврина Мария"

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# скрипт, создающий папки
import os

def make_dir(NewDir):
    if not NewDir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), NewDir)
    try:
        os.mkdir(dir_path)
        print("Директория {} создана".format(NewDir))
    except FileExistsError:
        print("Директория {} уже существует".format(NewDir))


# скрипт, удаляющий папки
def delete_dir(NewDir):
    if not NewDir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), NewDir)
    try:
        os.rmdir(dir_path)
        print("Директория {} удалена".format(NewDir))
    except FileExistsError:
        return False
    return
"""
for i in range(1, 10):
    NewDir = 'dir_' + str(i)
    make_dir(NewDir)
print("Директории созданы")

for i in range(1, 10):
    NewDir = 'dir_' + str(i)
    delete_dir(NewDir)
print("Директории удалены")

print("Задача 1 решена \n")
"""
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_dir():
    files = os.listdir(path = os.getcwd())
    return files
"""
files = show_dir()
print("Список файлов в текущей директории: \n", files)

for file in files:
    if os.path.isdir(file):
        print("Список папок текущей директории: \n", file)

print("Задача 2 решена \n")
"""
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
"""
import shutil
import sys

my_file = sys.argv[0]
my_file_copy = my_file + '.copy'
try:
    shutil.copy(my_file, my_file_copy)
except FileExistsError:
    print('Не удалось создать копию файла.')
print(my_file, my_file_copy)

print("Задача 3 решена \n")
"""