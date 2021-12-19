"""Дано матрицю A. Знайти матрицю транспоновану до даної."""
import random
n = int(input("n= "))
m = int(input("m= "))
a = [
    [random.randint(-100, 100) for j in range(m)] for i in range(n)
]
b = [
    [a[j][i] for j in range(len(a))] for i in range(len(a)-1 if n > m else len(a)+1)
]
print(b)