"""Дано текстовий файл, який містить дійсні числа. Визначити найбільший елемент серед від’ємних."""
import random
import pickle
n = int(input("n= "))
a = [random.randint(-10, 10) for i in range(n)]
with open("my.txt", "wb") as file:
    pickle.dump(a, file)
with open("my.txt", "rb") as file:
    b = pickle.load(file)
print(b)
max = -10
for el in b:
    if el < 0:
        if max < el:
            max = el
print("Найбільший елемент серед від’ємних: {0}".format(max))