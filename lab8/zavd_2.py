"""Трикутник задано координатами своїх вершин на площині. Використовуючи підпрограму для знаходження кута між векторами
на площині, встановити тип трикутника (гострокутний, прямокутний, тупокутний)."""
import random
import math
n = int(input("n= "))
a = [random.randint(-100, 100) for i in range(n)]
b = [random.randint(-100, 100) for i in range(n)]
print(a)
print(b)
def scal_dob_vectoriv(a, b):
    scal_dob = 0
    for i in range(len(a)):
        scal_dob += a[i] * b[i]
    return scal_dob
def dovz_vectora_1(a):
    dovz_vectora_a = 0
    for i in range(len(a)):
        dovz_vectora_a += a[i] ** 2
    return dovz_vectora_a
def dovz_vectora_2(b):
    dovz_vectora_b = 0
    for i in range(len(b)):
        dovz_vectora_b += b[i] ** 2
    return dovz_vectora_b
c = scal_dob_vectoriv(a, b) / (math.sqrt(dovz_vectora_1(a)) * math.sqrt(dovz_vectora_2(b)))
if math.cos(c) > 0:
    print("Гострокутний")
elif math.cos(c) == 0:
    print("Прямокутний")
else:
    print("Тупокутний")