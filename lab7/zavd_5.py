"""Переставляючи стовпці даної цілочислової матриці, розташувати їх у відповідності з ростом характеристик.
Характеристикою стовпця цілочислової матриці назвемо суму модулів його від’ємних непарних елементів."""
import random
n = int(input("n= "))
m = int(input("m= "))
a = [[random.randint(-10, 10) for j in range(m)] for i in range(n)]
print(*a, sep="\n")
b = []
c = list(zip(*a))
for j in range(m):
    sum = 0
    for i in range(n):
        for k in range(n):
            if a[i][j] < 0:
                sum += abs(a[i][j])
                break
    b += [sum]
    for i in range(len(b),0, -1):
        for j in range(0, len(b) - 1):
            if b[j] > b[j+1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                c[j], c[j + 1] = c[j + 1], c[j]
a = zip(*c)
print(*a,sep="\n")
