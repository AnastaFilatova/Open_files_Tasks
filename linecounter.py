# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
from pprint import pprint


def text_sort_by_line():
    """ объединяет текст из трех файлов по количеству строк"""

    with open('1.txt', encoding='UTF-8') as t1:
        text1 = t1.readlines()

    with open('2.txt', encoding='UTF-8') as t2:
        text2 = t2.readlines()

    with open('3.txt', encoding='UTF-8') as t3:
        text3 = t3.readlines()



    pprint(len(text3))


text_sort_by_line()