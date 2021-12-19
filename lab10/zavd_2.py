"""Об’єкт “Монітор”
поля: фірма виробник; дата виробництва; дата купівлі; вартість; тип монітора; розміри монітора
методи
визначення «віку» монітора;
визначення того, чи можна вивести зображення на моніторі без масштабування;
визначення коефіцієнтів масштабування при виведенні зображення як із збереженням пропорції так і без збереження пропорції.
"""
from datetime import date, datetime
def get_today_date():
    return date(datetime.today().year, datetime.today().month, datetime.today().day)
class Monitor():
    def __init__(self, firm, date_of_manu: date, date_of_purch, cost, type_of_monit, size_of_monit):
        self.firm = firm
        self.date_of_manu = date_of_manu
        self.date_of_purch = date_of_purch
        self.cost = cost
        self.type_of_monit = type_of_monit
        self.size_of_monit = size_of_monit
    def age(self):
        return get_today_date().year - self.date_of_manu.year
    def scale(self):
        if size_of_monit == size_of_picture:
            return("Без")
        else:
            return("З")
    def coeff(self):
        return size_of_monit[0] / size_of_picture[0], size_of_monit[1] / size_of_picture[1]
date_of_menu = date(2019, 5, 16)
size_of_monit = [1920, 1200]
monit = Monitor(input("Фірма виробник: "),date_of_menu, input("Дата купівлі:"),float(input('Вартість:')),
        input('Тип монітора: '), size_of_monit)
size_of_picture = [int(input("Розмір зображення: "))for i in range(2)]
print(" Фірма виробник: {0}\n Дата виробництва: {1}\n Дата купівлі: {2}\n Вартість: {3:.2f}$\n Тип монітора{4}\n"
      "Розміри монітора: {5},".format(monit.firm, monit.date_of_manu, monit.date_of_purch,
        monit.cost, monit.type_of_monit, monit.size_of_monit))
print("Вік монітору: {0} роки".format(monit.age()))
print(monit.scale())
print("Коефіцієнт масштабування".format(monit.coeff()))