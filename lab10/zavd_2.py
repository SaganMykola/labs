"""Об’єкт “Монітор”
поля: фірма виробник; дата виробництва; дата купівлі; вартість; тип монітора; розміри монітора"""
class Monitor():
    def __init__(self, firm, date_of_manu, date_of_purch, cost, type, size):
        self.firm = firm
        self.date_of_manu = date_of_manu
        self.date_of_purch = date_of_purch
        self.cost = cost
        self.type = type
        self.size = size
monit = Monitor(input('Фірма виробник: ') , input('Дата виробництва: '), input('Дата купівлі: '),
float(input('Вартість:')), input('Тип монітора:'), input('Розміри монітора: '))
print(" Фірма виробник: {0}\n Дата виробництва: {1}\n Дата купівлі: {2}\n Вартість: {3:.2f}$\n Тип монітора{4}\n"
       "Розміри монітора: {5}".format(monit.firm, monit.date_of_manu, monit.date_of_purch, monit.cost, monit.type, monit.size))