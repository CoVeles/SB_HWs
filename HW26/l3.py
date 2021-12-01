import os
import os.path as path


def gen_files_path(initial_path: str, find_path: str):
    for cur_object in os.listdir(initial_path):
        cur_path = path.join(initial_path, cur_object)
        if path.isfile(cur_path):
            yield cur_path
        elif cur_path.endswith(find_path):
            print('Каталог найден:', cur_path)
            return


initial_path = os.path.abspath(os.sep)
find_path = input('Введите название искомого каталога: ')
seek = gen_files_path(initial_path, find_path)
for element in seek:
    print(element)
