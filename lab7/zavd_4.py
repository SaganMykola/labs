"""Розмістити елементи непарних стовпців у порядку спадання."""
import random
n = int(input("n= "))
m = int(input("m= "))
a = [
    [random.randint(0, 9) for j in range(m)] for i in range(n)
]
print(*a, sep = "\n")
for j in range(1,m,2):
    for i in range(n):
        for k in range(n):
            if a[i][j] < a[k][j]:
                c = a[k][j]
                a[k].insert(j,a[i][j])
                a[i].insert(j,c)
                a[i].pop(j+1)
                a[k].pop(j+1)
print(*a, sep = "\n")