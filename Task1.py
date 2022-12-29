""" A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
 """


from random import randint

def create_index_list (k):
    index_list = [randint(0,100) for i in range (k+1)]
    if index_list[len(index_list) - 1] == 0:
        index_list[len(index_list) - 1] == randint(1,100)
    return index_list

def create_polynom (index_list):
    polynom = ''
    k = len(index_list) - 1
    i = len(index_list) - 1
    while (i > 1):
        if index_list[i] !=0 and index_list[i] !=1:
            polynom = polynom + '{}x^{} + '.format(index_list[i], i)
        elif index_list[i] == 0:
            polynom = polynom + ''
        elif index_list[i] == 1:
            polynom = polynom + 'x^{} + '.format(i)
        i = i -1
    polynom = polynom + '{}x + {} = 0'.format(index_list[1], k)
    print(polynom)
    return polynom

def write_polynom_1():
    k = int(input('Введите степень первого многочлена: '))
    poly = create_polynom(create_index_list(k))
    with open('polynom1.txt', 'w') as data:
        data.write(poly)

def write_polynom_2():
    k = int(input('Введите степень второго многочлена: '))
    poly = create_polynom(create_index_list(k))
    with open('polynom2.txt', 'w') as data:
        data.write(poly)

write_polynom_1()

write_polynom_2()