"""Знайти суму елементів в тих стовпцях, які містять хоча б один від’ємний елемент такі k, що k-й рядок матриці
співпадає з k-м стовбцем"""
import random
n = int(input("n= "))
m = int(input("m= "))
a = [[random.randint(-10, 10) for j in range(m)] for i in range(n)]
print(*a, sep = "\n")
c = []
for i in range(n if n <= m else m):
    if a[i][i] < 0:
        x = a[i][i]
        c += [x]
    else:
        c += [0]
print(c)
for j in range(n if n <= m else m):
    sum = 0
    if c[j] < 0:
        for i in range(n if n <= m else m):
            for k in range(n if n <= m else m):
                sum += a[i][j]
                break
        print('Сума елементів в стовпці {0} , який містять хоча б один від’ємний елемент елемент такі k,'
              ' що k-й рядок матриці співпадає з k-м стовбцем: {1}'.format(j, sum))