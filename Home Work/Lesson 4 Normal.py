# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# def fibonacci(n, m):

def fib(n, m):
    i = 1
    fib_list=[1,1]
    while i < m:
        fib_list.append(fib_list[i-1] + fib_list[i])
        i += 1
    return fib_list[n:m]

print(fib(1,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# def sort_to_max(origin_list):
#    pass
#sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

def sort_to_max(origin_list):
    n = len(origin_list)
    for i in range(0,n-1):
        for j in range(i  +1, n):
            if origin_list[i] > origin_list[j]:
                origin_list[i],origin_list[j] = origin_list[j], origin_list[i]
                return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

