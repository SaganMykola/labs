"""Дано дійсні числа x,y,z . Обчислити"""
import random
x = random.randint(-10,10)
y = random.randint(-10,10)
z = random.randint(-10,10)
def max_1(x, y, z):
    return max(x, y, z) + max(x + y, x * y, 4 * z)
def max_2(x, y, z):
    return max(max(x + y, x * y, x ** 2) ** 2, 7, z ** 2)
a = max_1(x, y, z)
b = max_2(x, y, z)
div = a / b
print("Відповідь: {0:.2f}".format(div))