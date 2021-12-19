"""Побудувати квадратну матрицю А, елементи якої задаються формулою:
a[i][j]=sin((i^2-j^2)/n), i, j = 1, N
Знайти найбільший за модулем елемент матриці А та його індекси."""
import math
n = int(input("n= "))
a = [
    [math.sin((i**2 - j**2) / n) for j in range(n)] for i in range(n)
]
max = a[0][0]
for i in a:
    for el in i:
        if max < el:
            max = el
print("Max= {0}".format(max))