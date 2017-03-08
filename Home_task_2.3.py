# -*- coding: utf-8 -*-
import json
import yaml

recipes_book = {
    'яичница': [
        {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        ],
    'стейк': [
        {'ingredient_name': 'говядина', 'quantity': 300 , 'measure': 'гр.'},
        {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        ],
    'салат': [
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
        ]
    }

with open('Book_cook.json', 'w', encoding='utf-8') as f:
    json.dump(recipes_book, f, ensure_ascii=False, indent=2)

with open('Book_cook.yml', 'w', encoding='utf-8') as f:
    yaml.dump(recipes_book, f, default_flow_style=False, allow_unicode=True, indent=2)

with open('Book_cook.json', 'r') as f:
    json_data = json.load(f)
    for line in f.readlines():
        print(line.strip())