# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not some_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), some_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(some_name))
    except FileExistsError:
        print('директория {} уже существует'.format(some_name))


def ping():
    print("pong")


def cp():
    file_path = os.path.join(os.getcwd(), some_name)
    if os.path.exists(file_path):
        shutil.copyfile(file_path, file_path + '_cp')
    else:
        print(f"Файл {file_path} не существует")


def rm():
    file_path = os.path.join(os.getcwd(), some_name)
    if os.path.exists(file_path):
        answer = input("Подтвердите удаление (д/н):")
        if answer == 'д':
            try:
                os.remove(file_path)
            except Exception as ex:
                print(f"Хьюстон, у нас проблемы: {type(ex).__name__}")
    else:
        print(f"Папка {some_name} не существует")


def cd():
    if os.path.exists(some_name):
        os.chdir(some_name)
        print(os.listdir(some_name))
    else:
        print(f"Папка {some_name} не существует")


def ls():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    some_name = sys.argv[2]
except IndexError:
    some_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
