from pprint import pprint

file_name = 'cookbook.txt'

def read_cookbook(file_name):
    with open(file_name) as f:
        cook_book = {}
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