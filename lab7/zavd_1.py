"""Визначити добуток додатних елементів матриці нижче головної діагоналі."""
import random
n = int(input("n= "))
m = int(input("m= "))
a = [
    [random.randint(-100, 100) for j in range(m)] for i in range(n)
]
print(*a, sep="\n")
s = []
for j in range(len(a)):
    for i in range(j+1, len(a)):
        x = a[i][j]
        s.append(x)
print(s)