from random import randint

class Deck:
    def __init__(self) -> None:
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suit = ["♣", "♦", "♠", "♥"]


    def generate_card(self):
        self.card = []

        self.card.append(self.suit[randint(0,3)])
        self.card.append(self.value[randint(0,12)])


    def print_card(self, card):
        if card[1] == "10":
            print('┌───────┐')
            print(f'| {card[1]}    |')
            print('|       |')
            print(f'|   {card[0]}   |')
            print('|       |')
            print(f'|    {card[1]} |')
            print('└───────┘')

        else:
            print('┌───────┐')
            print(f'| {card[1]}     |')
            print('|       |')
            print(f'|   {card[0]}   |')
            print('|       |')
            print(f'|     {card[1]} |')
            print('└───────┘')


a = Deck()