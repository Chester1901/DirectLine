# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['Яблоко', 'Банан', 'Киви', 'Арбуз']
a = len(fruits)
for i in range(a):
    print(str(i+1)+"."+"{:>7}".format(fruits[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = {1,4,6,8,10,12,25}
spisok2 = {2,4,5,8,9,10}
spisok3 = spisok1 - spisok2
print (spisok3)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

spisok = [2, 3, 4, 7, 8, 20]
new_spisok = []
for i in spisok:
    if i % 2 == 0:
        new_spisok.append(i/4)
    else:
        new_spisok.append(i*2)
print (new_spisok)
