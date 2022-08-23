from pprint import pprint

file_name = 'cookbook.txt'
cook_book = {}
def read_cookbook(file_name):
    with open(file_name, 'rt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            cook_book[dish_name] = []
            for i in range(int(f.readline())):
                comp = f.readline().split(' | ')
                cook_book[dish_name].append({'ingredient_name': comp[0],
                                             'quantity': int(comp[1]),
                                             'measure': comp[2].strip()})
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for comp in cook_book[dish]:
                if comp['ingredient_name'] in shop_list:
                    shop_list[comp['ingredient_name']]['quantity'] += comp['quantity'] * person_count
                else:
                    shop_list[comp['ingredient_name']] = {'measure': comp['measure'],
                                                          'quantity': (comp['quantity'] * person_count)}
    return shop_list

import os
files_list = ['1.txt', '2.txt', '3.txt']

def unite(files_list):
    path = os.getcwd()
    dir_list = os.listdir(path)
    files_dict = {}

    for file in files_list:
        if file in dir_list:
            with open(file, encoding='utf-8') as f:
                count = 0
                for line in f:
                    count += 1
                files_dict[file] = count

    sorted_tuple = sorted(files_dict.items(), key=lambda x: x[1])
    files_dict = dict(sorted_tuple)

    with open('united.txt', 'a', encoding='utf-8') as fw:
        for key, value in files_dict.items():
            fw.write(f'{key}\n{value}\n')
            with open(key, encoding='utf-8') as f:
                text = f.read()
                fw.write(f'{text}\n')

unite(files_list)










