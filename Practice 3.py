import random

class Card:  # класс Карта
    NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
    MastList = ["пики", "крести", "буби", "черви"]

    def __init__(self, i, j):  # конструктор
        self.Mastb = self.MastList[i - 1]  # масть
        self.Num = self.NumsList[j - 1]    # номер

class DeckOfCards:  # класс Колода карт
    def __init__(self):  # конструктор
        self.deck = [None] * 56  # список из 56 карт
        k = 0
        for i in range(1, 5):
            for j in range(1, 14):
                self.deck[k] = Card(i, j)  # очередная карта
                k += 1

    def shuffle(self):  # перемешивание карт
        random.shuffle(self.deck)

    def get(self, i):  # вытаскивание i-й карты из колоды
        if 0 <= i < 56:
            answer = f'{self.deck[i].Num} {self.deck[i].Mastb}'
        else:
            answer = "В колоде только 56 карт"
        return answer

deck = DeckOfCards()  # создали колоду
deck.shuffle()  # перемешали
print('Выберите карту из колоды (1-56):')
n = int(input())
if 1 <= n <= 56:
    card = deck.get(n - 1)
    print('Вы взяли карту:', card)
else:
    print("В колоде только 56 карт")