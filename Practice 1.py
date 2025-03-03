class Planet():
    ylC=5000000
    sbmax=100000000

    def __init__(self, name, rang, co, mar):
        self.name = name
        self.rang = rang
        self.co = co
        self.mar = mar
        self.costs = {}

    def addcost(self, *val):
        for i in val:
            self.costs[i[0]] = i[1]

    def costsf(self):
        s = Planet.ylC * 2 * self.rang + Planet.sbmax * self.co
        if bool(self.costs):
            for i in self.costs.values():
                s += i
        return s

    def income(self):
        return self.mar * Planet.sbmax

    def profit(self):
        return self.income() - self.costsf()

    def __str__(self):
        return f'{"Информация о планете":>25} {self.name:<}\n' \
               f'{"Расходы:":>25} {self.costsf():<}\n' \
               f'{"Доходы:":>25} {self.income():<} \n' \
               f'{"Прибыль:":>25} {self.profit():<}'

pl = Planet('Mars', 100, 10, 25)
pl.addcost(('Охрана', 20000000), ('Оборудование', 300000000))
print(pl)