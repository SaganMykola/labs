"""У типізованому файлі міститься двовимірний масив цілих чисел. Спочатку записано кількість рядків та кількість стовпців.
Визначити найбільший елемент цього масиву, використовуючи динамічно створений масив для збереження цього масиву."""
import random
import pickle
n = int(input("n= "))
m = int(input("m= "))
a = [[random.randint(-10, 10) for j in range(m)] for i in range(n)]
with open("matrix.txt", "wb") as f:
    pickle.dump(a, f)
with open("matrix.txt", "rb") as f:
    b = pickle.load(f)
print(b)
max = b[0][0]
for i in range(len(a)):
    for j in range(len(a)):
        if max < b[i][j]:
            max = b[i][j]
print("Найбільший елемент масиву: {0}".format(max))