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
        print("Папка {} успешно создана".format(NewDir))
    except FileExistsError:
        print("Папка {} уже существует".format(NewDir))


# скрипт, удаляющий папки
def delete_dir(NewDir):
    if not NewDir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), NewDir)
    try:
        os.rmdir(dir_path)
        print("Папка {} успешно удалена".format(NewDir))
    except FileExistsError:
        print("Невозможно удалить {}. Возможно такой не существует".format(NewDir))
    return

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_dir():
    files = os.listdir(path = os.getcwd())
    return files

def transition_dir(NewDir):
    if not NewDir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), NewDir)
    try:
        os.chdir(dir_path)
        print("Переход в папку {} успешно завершен".format(NewDir))
    except FileExistsError:
        print("Невозможно перейти в папку. Возможно такой не существует")
    return