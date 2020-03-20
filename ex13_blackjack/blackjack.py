"""Blackjack."""
import importlib
import os
import pkgutil
from deck import Deck, Card
from game_view import GameView, FancyView, Move
from strategy import Strategy, HumanStrategy, MirrorDealerStrategy


class Hand:
    """Hand."""

    def __init__(self, cards: list = None):
        """Init."""
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
        self.is_double_down = False
        self.is_surrendered = False

    def add_card(self, card: Card) -> None:
        """Add card to hand."""
        self.cards.append(card)

    def double_down(self, card: Card) -> None:
        """Double down."""
        self.add_card(card)
        self.is_double_down = True

    def split(self):
        """Split hand."""
        if self.can_split:
            return Hand([self.cards.pop(0)])
        raise ValueError("Invalid hand to split!")

    @property
    def can_split(self) -> bool:
        """Check if hand can be split."""
        copies = 0
        for i in range(len(self.cards)):
            for j in range(i + 1, len(self.cards)):
                if self.cards[i] == self.cards[j]:
                    copies += 1

        if copies == 1:
            return True
        else:
            return False

    @property
    def is_blackjack(self) -> bool:
        """Check if is blackjack."""
        v = [cards.value for cards in self.cards]
        if len(self.cards) != 2:
            return False
        else:
            if 'ACE' in v and ('10' in v or 'JACK' in v or 'QUEEN' in v or 'KING' in v):
                return True
            return False

    @property
    def is_soft_hand(self):
        """Check if is soft hand."""
        for val in self.cards:
            if val.value == 'ACE':

                if (self.score + 10) >= 21:
                    return True

        return False

    @property
    def score(self) -> int:
        """Get score of hand."""
        summa = 0
        for i in self.cards:

            if len(i.value) > 3:
                weight = 10
            elif i.value == 'ACE':
                weight = 11
            else:
                weight = int(i.value)
            summa += weight

            # Дикая игра с тузами
            if summa > 21:
                summa -= 10

        return summa


class Player:
    """Player."""

    def __init__(self, name: str, strategy: Strategy, coins: int = 100):
        """Init."""
        self.hands = []
        self.name = name
        self.strategy = strategy
        self.coins = coins
        # strategy.player = self

    def join_table(self):
        """Join table."""
        pass

    def play_move(self, hand: Hand) -> Move:
        """Play move."""
        return self.strategy.play_move(hand)

    def split_hand(self, hand: Hand) -> None:
        """Split hand."""
        self.hands.append(hand.split)


class GameController:
    """Game controller."""

    PLAYER_START_COINS = 200
    BUY_IN_COST = 10

    def __init__(self, view: GameView):
        """Init."""
        # self.house = Hand()
        self.house = []
        self.players = []
        self.deck = None
        self.view = view

    def start_game(self) -> None:
        """Start game."""
        deck = self.view.ask_decks_count()
        self.deck = Deck(deck)
        player = self.view.ask_players_count()
        for p in range(player):
            name = self.view.ask_name(p)
            play = Player(name, HumanStrategy(self.players, self.house, self.deck.deck_count, self.view), GameController.PLAYER_START_COINS)
            self.players.append(play)
        bot = self.view.ask_bots_count()
        for p in range(bot):
            name = self.view.ask_name(p)
            play = Player(name, MirrorDealerStrategy(self.players, self.house, self.deck.deck_count), GameController.PLAYER_START_COINS)
            self.players.append(play)

    def check_players(self):
        """Check players."""
        active = []
        for p in self.players:
            if p.coins > 10:
                active.append(p)
        return active

    def init_round(self, players):
        """Init round."""
        for i in range(2):
            for player in players:
                player.hands[0].add_card(self.deck.draw_card())
            self.house.append(self._draw_card(i == 0))

    def make_moves(self, players: list):
        """Make moves."""
        for play in players:
            for hand in play.hands:
                move = play.play_move(hand)
                if move == Move.HIT:
                    self._draw_card()
                elif move == Move.DOUBLE_DOWN:
                    self._draw_card()
                    # Check value of coins. Double
                elif move == Move.SPLIT:  # Control, can i?
                    if Hand.split(hand):
                        break
                    move = play.play_move(hand)
                    break
                elif move == Move.STAND:
                    break
                elif move == Move.SURRENDER:
                    pass

    def money(self, players):
        """Money count."""
        for p in players:  # Check house. Win, fail, draw. Surrender!
            pass

    def play_house(self):
        """House."""
        self.house.add_card(self._draw_card())
        if self.house.score < 17:
            self.house = self._draw_card()

    def play_round(self) -> bool:
        """Play round."""
        players = self.check_players()
        self.init_round(players)
        self.make_moves(players)
        self.play_house()
        self.money(players)

    def _draw_card(self, top_down: bool = False) -> Card:
        """Draw card."""
        deck = self.view.ask_decks_count()
        self.deck = Deck(deck)
        return Deck.draw_card(Deck(deck, top_down))

    @staticmethod
    def load_strategies() -> list:
        """
        Load strategies.

        @:return list of strategies that are in same package.
        DO NOT EDIT!
        """
        pkg_dir = os.path.dirname(__file__)
        for (module_loader, name, is_pkg) in pkgutil.iter_modules([pkg_dir]):
            importlib.import_module(name)
        return list(filter(lambda x: x.__name__ != HumanStrategy.__name__, Strategy.__subclasses__()))


if __name__ == '__main__':
    game_controller = GameController(FancyView())
    game_controller.start_game()
    while game_controller.play_round():
        pass
