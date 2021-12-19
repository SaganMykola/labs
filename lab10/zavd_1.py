"""Об’єкт “Пряма на площині ”
поля: для зберігання коефіцієнтів канонічного рівняння прямої;
методи: введення та виведення коефіцієнтів;
        знаходження точки перетину з іншою прямою;
        встановлення паралельності з іншою прямою;
        встановлення належності деякої точки прямій."""
import random
class Straight():
    def __init__(self, line_1, line_2):
        self.line_1 = line_1
        self.line_2 = line_2
    def Intersection_point(self):
        xdiff = (self.line_1[0][0] - self.line_1[1][0], self.line_2[0][0] - self.line_2[1][0])
        ydiff = (self.line_1[0][1] - self.line_1[1][1], self.line_2[0][1] - self.line_2[1][1])
        def deter(a, b):
            return a[0] * b[1] - a[1] * b[0]
        frac = deter(xdiff, ydiff)
        if frac == 0:
            print("Паралельна з іншою прямою")
            return "Точка перетину відсутня"
        else:
            d = (deter(*self.line_1), deter(*self.line_2))
            x = deter(d, xdiff) / frac
            y = deter(d, ydiff) / frac
            print("Не паралельна з іншою прямою")
            return x, y
    def Bel(self):
        xdiff = [(self.line_1[0][0] - self.line_1[1][0])]
        ydiff = [(self.line_1[0][1] - self.line_1[1][1])]
        d = [float(input("A= ")) for i in range(2)]
        dob = (xdiff[0] * d[0]) / ydiff[0]
        if d[0] == dob:
            return "Точка належить прямій"
        else:
            return "Точка не належить прямій"
lines = Straight([[random.randint(-10, 10) for j in range(2)] for i in range(2)]
                 , [[random.randint(-10, 10) for j in range(2)] for i in range(2)])
print("Точка перетину з іншою прямою: {0}".format(lines.Intersection_point()))
print("Встановлення належності деякої точки прямій: {0}".format(lines.Bel()))