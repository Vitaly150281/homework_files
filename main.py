from pprint import pprint

file_name = 'cookbook.txt'
cook_book = {}
def read_cookbook(file_name):
    with open(file_name) as f:
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

