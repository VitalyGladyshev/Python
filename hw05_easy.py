# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


def dir_1_9_create():
    err_dir_list = []
    this_dir = os.getcwd()
    for ind in range(1, 10):
        dir_path = os.path.join (this_dir, 'dir_' + str(ind))
        if os.path.exists(dir_path):
            err_dir_list.append('dir_' + str(ind))
        else:
            os.mkdir(dir_path)
            os.makedirs
    return err_dir_list


def dir_1_9_delete():
    err_dir_list = []
    this_dir = os.getcwd()
    for ind in range(1, 10):
        dir_path = os.path.join (this_dir, 'dir_' + str(ind))
        if os.path.exists(dir_path):
            try:
                os.rmdir(dir_path)
            except Exception as ex:
                err_dir_list.append("dir_{} {}".format(ind, type(ex).__name__))
    return err_dir_list


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_cur_dir():
    for roots, dirs, files in os.walk(os.getcwd()):
        return dirs


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def this_file_copy():
    shutil.copyfile(str(sys.argv)[2:-2], str(sys.argv)[2:-2] + '_cp')
    return str(sys.argv)[2:-2] + '_cp'


if __name__ == "__main__":
    print("Задача-1")

    res_dir_create = dir_1_9_create()
    if res_dir_create:
        print("Директории: {} уже существуют".format(res_dir_create))
    else:
        print("Директории успешно созданы")

    print(list_cur_dir())
    res_dir_delete = dir_1_9_delete()
    if res_dir_delete:
        print("Не все директории удалены: ", res_dir_delete)
    else:
        print("Директории успешно созданы")

    print("\nЗадача-2")
    print(list_cur_dir())

    print("\nЗадача-3")
    print(this_file_copy())
