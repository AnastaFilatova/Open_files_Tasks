# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#     'Фахитос': [
#     {'ingredient_name': 'Говядина ', 'quantity': 500, 'measure': ' г'},
#     {'ingredient_name': 'Перец сладкий ', 'quantity': 1, 'measure': ' шт'},
#     {'ingredient_name': 'Лаваш ', 'quantity': 2, 'measure': ' шт'},
#     {'ingredient_name': 'Винный уксус ', 'quantity': 1, 'measure': ' ст.л'},
#     {'ingredient_name': 'Помидор ', 'quantity': 2, 'measure': ' шт'}
#   }
from pprint import pprint


def cookbook():
    """ Создание словаря рецептов из текстового файла"""

    cook_book = {}
    with open('recipes.txt', encoding='UTF-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            count = int(f.readline())
            ingr_list = list()
            for i in range(count):
                ingr = f.readline().strip()
                # print(ingr)
                splited_ingr = ingr.split(' | ')
                ingr_dict = {
                    'ingredient_name': splited_ingr[0],
                    'quantity': int(splited_ingr[1]),
                    'measure': splited_ingr[2]
                }
                ingr_list.append(ingr_dict)
            f.readline().strip()
            cook_book[dish_name] = ingr_list
    return cook_book



# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    """ Задание 2 """

    cookbook_dict = cookbook()
    ingredients = {}
    quant = {}
    #print(dishes)
    for dish in dishes:
        # print(dish)
        if dish in cookbook_dict.keys():
            for ingr_dic in cookbook_dict[dish]:
                # print(ingr_dic)
                # print(ingredients)
                if ingr_dic['ingredient_name'] not in ingredients:
                    ingredients[ingr_dic['ingredient_name']] = {}
                    measure = {'measure': ingr_dic['measure']}
                    # print(measure)
                    ingredients[ingr_dic['ingredient_name']].update(measure)
                    # print(ingredients)
                    quant = {'quantity': ingr_dic['quantity'] * person_count}

                else:
                    quant['quantity'] = ingredients[ingr_dic['ingredient_name']]['quantity']
                    quant['quantity'] += ingr_dic['quantity'] * person_count   # 1 var

                ingredients[ingr_dic['ingredient_name']].update(quant)

    return ingredients




pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# У вас количество тянется из условия if (последнее в цикле = 100) даже когда программа переходит к выполнению условия else.
# А нужно при этом брать количество из уже имеющегося у вас в словаре.
# Добавьте сразу после else: вот эту строку quant['quantity'] = ingredients[ingr_dic['ingredient_name']]['quantity']