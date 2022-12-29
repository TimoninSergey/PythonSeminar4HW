""" B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

 """

import re


def read_polynom(file_name):
    with open(str(file_name), 'r') as data:
        polynom = data.read()
    return polynom

def create_koef_list1 (x_list1):
    koef_list1 = []
    for i in range(len(x_list1)):
        if 'x^' in x_list1[i]:
            koef_list1.append(x_list1[i].split('x'))
        elif 'x' in x_list1[i]:
            koef_list1.append(x_list1[i].split('x'))
            koef_list1[i].remove('')
            koef_list1[i].append('^1')
        elif 'x' not in x_list1[i]:
            koef_list1.append([x_list1[i], '^0'])
    return koef_list1

def create_koef_list2 (x_list2):
    koef_list2 = []
    for i in range(len(x_list2)):
        if 'x^' in x_list2[i]:
            koef_list2.append(x_list2[i].split('x'))
        elif 'x' in x_list2[i]:
            koef_list2.append(x_list2[i].split('x'))
            koef_list2[i].remove('')
            koef_list2[i].append('^1')
        elif 'x' not in x_list2[i]:
            koef_list2.append([x_list2[i], '^0'])
    return koef_list2

def create_final_koef_list (koef_list1, koef_list2):
    koef_list3 = []
    delete_list1 = []
    delete_list2 = []
    for k in range(len(koef_list1)):
        for j in range(len(koef_list2)):
            if koef_list1[k][1] == koef_list2[j][1]:
                koef_list3.append([int(koef_list1[k][0]) + int(koef_list2[j][0]), koef_list1[k][1]])
                delete_list1.append(koef_list1[k])
                delete_list2.append(koef_list2[j])
    for i in koef_list1:
        if i not in delete_list1:
            koef_list3.append(i)
    for i in koef_list2:
        if i not in delete_list2:
            koef_list3.append(i)
    koef_list_final = []
    for n in range(len(koef_list3)):
        koef_list_final.append([koef_list3[n][0], int(koef_list3[n][1].replace('^',''))])
    koef_list_final.sort(key=lambda tup: tup[1], reverse=True)
    return koef_list_final

def create_final_polynom (koef_list_final):
    final_polynom = ''
    for n in koef_list_final:
        if n[1] !=1 and n[1] !=0:
            final_polynom = final_polynom + str(n[0]) + 'x^' + str(n[1]) + ' + '
        elif n[1] == 1:
            final_polynom = final_polynom + str(n[0]) + 'x' + ' + '
        elif n[1] == 0:
            final_polynom = final_polynom + str(n[0]) + ' = 0'
    return final_polynom

polynom1 = read_polynom('polynom1.txt')
polynom1 = polynom1.replace(' = 0', '')
x_list1 = polynom1.split(sep=' + ')

polynom2 = read_polynom('polynom2.txt')
polynom2 = polynom2.replace(' = 0', '')
x_list2 = polynom2.split(sep=' + ')

koef_list_final = create_final_koef_list(create_koef_list1 (x_list1), create_koef_list2 (x_list2))
final_polynom = create_final_polynom(koef_list_final)

with open('final_polynom.txt', 'w') as data:
        data.write(final_polynom)

print(final_polynom)