"""Deck."""
from typing import Optional, List
import requests
import random


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str, top_down=False):
        """Constructor."""
        self.value = value
        self.suit = suit
        self.code = code
        self.top_down = top_down

    def __str__(self):
        """Str."""
        if self.top_down is False:
            return self.code
        return "??"

    def __repr__(self) -> str:
        """Repr."""
        return self.code

    def __eq__(self, o) -> bool:
        """Eq."""
        if self.suit == o.suit and self.value == o.value:
            return True
        return False


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"
    codes = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS',
             'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
             'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
             'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH']
    values = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    suits = ['SPADES', 'DIAMONDS', 'CLUBS', 'HEARTS']

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        if shuffle:
            r = requests.get(self.DECK_BASE_API + f"new/shuffle/?deck_count={deck_count}").json()
        else:
            r = requests.get(self.DECK_BASE_API + f"new/?deck_count={deck_count}").json()
        self.remaining = 52 * deck_count
        self.deck_count = deck_count
        self.is_shuffled = shuffle
        self._backup_deck = self._generate_backup_pile(self.is_shuffled, self.deck_count)
        self.deck_id = r.get("deck_id")

    def shuffle(self) -> None:
        """Shuffle the deck."""
        requests.get(self.DECK_BASE_API + f'{self.deck_id}/shuffle/?deck_count=1').json()

    def draw_card(self, top_down: bool = False) -> Optional[Card]:
        """
        Draw card from the deck.

        :return: card instance.
        """
        url = f"{Deck.DECK_BASE_API}{self.deck_id}/draw/?count=1"
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            result = r.json()
            if result.get("success", False) is True:
                if self.remaining > 0:
                    card = result["cards"][0]
                    new_card = Card(card["value"], card["suit"], card["code"], top_down)
                    if new_card in self._backup_deck:
                        self._backup_deck.remove(new_card)
                        self.remaining -= 1
                    return new_card
        else:
            if self.remaining != 0:
                new_card = self._backup_deck[0]
                self._backup_deck.remove(new_card)
                self.remaining -= 1
                return new_card

    def _request(self, url: str) -> dict:
        """Update deck."""
        return requests.get(url).json()

    @staticmethod
    def _generate_backup_pile(is_shuffled, deck_count) -> List[Card]:
        """Generate backup pile."""
        if is_shuffled is False:
            backup_deck = []
            for i in range(deck_count):
                for c in range(52):
                    backup_deck.append(Card(Deck.values[c % 13], Deck.suits[c // 13], Deck.codes[c]))
            return backup_deck
        else:
            backup_deck = []
            for c in range(deck_count):
                for i in range(52):
                    backup_deck.append(Card(Deck.values[i % 13], Deck.suits[i // 13], Deck.codes[i]))
            random.shuffle(backup_deck)
            return backup_deck


if __name__ == '__main__':
    d = Deck(shuffle=False)
    print(d.remaining)  # 52
    card1 = d.draw_card()  # Random card
    print(card1 in d._backup_deck)  # False
    print(d._backup_deck)  # 51 shuffled cards
    d2 = Deck(deck_count=2)
    print(d2._backup_deck)  # 104 ordered cards (deck after deck)
