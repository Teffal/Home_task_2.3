# -*- coding: utf-8 -*-
import json
import yaml
import os
# Ver. 2017.03.21


def file_cook_book(my_file_path):
    if my_file_path.endswith('.json'):
        with open(my_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        with open(my_file_path, 'r', encoding='utf-8') as f:
            return yaml.load(f)


def get_shop_list_by_dishes(dishes, person_count, my_file_path):
    shop_list = {}
    for dish in dishes:
        print(file_cook_book(my_file_path))
        for ingridient in file_cook_book(my_file_path)[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingredient_name}: {quantity} {measure} '.format(**shop_list_item))


def create_shop_list():
    my_file_path = input('Enter the path to your file (default path: Book_cook.json):')
    if not my_file_path:
        my_file_path = 'Book_cook.json'
    person_count = int(input('Enter count of person: '))
    dishes = input('Enter dishes for one person (you can list separated by "," without space): ').lower().split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count, my_file_path)
    print_shop_list(shop_list)

create_shop_list()
