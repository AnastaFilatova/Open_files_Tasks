# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
from pprint import pprint


def text_sort_by_line():
    """ объединяет текст из трех файлов по количеству строк"""

    cooment_text = {}

    with open('1.txt', encoding='UTF-8') as t1:
        text1 = t1.readlines()
        cooment_text[len(text1)] = ['1.txt', text1]

    with open('2.txt', encoding='UTF-8') as t2:
        text2 = t2.readlines()
        cooment_text[len(text2)] = ['2.txt', text2]

    with open('3.txt', encoding='UTF-8') as t3:
        text3 = t3.readlines()
        cooment_text[len(text3)] = ['3.txt', text3]

    with open('union_text.txt', 'a', encoding='UTF-8') as union:
        list_long = list(cooment_text.keys())
        list_long.sort()
        for i in list_long:
            union.write(f'{cooment_text[i][0]}\n')
            union.write(f'{str(i)}\n')
            union.write(f'{"".join(cooment_text[i][1])}\n')

    return


text_sort_by_line()
