from random import randint

class Deck:
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUIT = ["♣", "♦", "♠", "♥"]

    deck = {}
    card = []

    def getDeck(self) -> dict:
        return self.deck

    def setDeck(self, deck: dict) -> None:
        self.deck = deck

    def getCard(self) -> list:
        return self.card

    def setCard(self, card: list) -> None:
        self.card = card

    def generateDeck(self) -> None:
        deck = {}

        for s in self.SUIT:
            deck[s] = []

        for key in deck.keys():
            deck[key] = self.VALUES

        self.setDeck(deck)

    def generateCard(self) -> bool:
        deck = self.getDeck()
        card = []

        if len(deck.keys()) != 0:
            card.append(self.SUIT[randint(0, len(deck.keys()) - 1)])
            card.append(self.VALUES[randint(0, len(deck[card[0]]) - 1)])

            deck[card[0]].remove(card[1])

            if len(deck[card[0]]) == 0:
                deck.pop(card[0])

            self.setDeck(deck)
            self.setCard(card)

            return True

        return False

    def printCard(self, card: list) -> None:
        if card[1] == "10":
            print('┌───────┐')
            print(f'| {card[1]}    |')
            print('|       |')
            print(f'|   {card[0]}   |')
            print('|       |')
            print(f'|    {card[1]} |')
            print('└───────┘')

            return

        print('┌───────┐')
        print(f'| {card[1]}     |')
        print('|       |')
        print(f'|   {card[0]}   |')
        print('|       |')
        print(f'|     {card[1]} |')
        print('└───────┘')
