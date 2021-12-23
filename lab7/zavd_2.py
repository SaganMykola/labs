"""Побудувати квадратну матрицю А, елементи якої задаються формулою:
a[i][j]=sin((i^2-j^2)/n), i, j = 1, N
Знайти найбільший за модулем елемент матриці А та його індекси."""
import math
n = int(input("n= "))
a = [
    [math.sin((i**2 - j**2) / n) for j in range(n)] for i in range(n)
]
print(*a, sep="\n")
max = abs(a[0][0])
for i in range(len(a)):
    for j in range(len(a)):
        if max < abs(a[i][j]):
            max = a[i][j]
            row = a.index(a[i])
            column = a.index(a[j])

print("Найбільший елемент за модулем= {0:.2f}, його індекс: [{1}][{2}]".format(max, row, column))