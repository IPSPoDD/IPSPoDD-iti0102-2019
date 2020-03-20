"""Pizzeria."""
from math import pi
from math import floor


class Chef:
    """Chef."""

    def __init__(self, name: str, experience_level: int):
        """
        Initialize chef.

        :param name:
        :param experience_level:
        """
        self.name = name
        self.experience_level = experience_level
        self.money = 0

    def __repr__(self):
        """
        Return str.

        :return:
        """
        return f'Pizza chef {self.name.capitalize()} with {self.experience_level} XP'


class Pizza:
    """Pizza."""

    def __init__(self, name: str, diameter: int, toppings: list):
        """
        Initialize pizza.

        :param name:
        :param diameter:
        :param toppings:
        """
        self.name = name
        self.diameter = diameter
        self.toppings = toppings

    def calculate_complexity(self) -> int:
        """
        Calculate complexity.

        :return:
        """
        complex = 0
        for top in self.toppings:
            complex += len(top) // 3
        return complex

    def calculate_price(self) -> int:
        """
        Calculate price.

        :return:
        """
        return floor((pi * (self.diameter / 2) * (self.diameter / 2) / 40 + (len(self.toppings)) // 2) * 100)

    def __repr__(self):
        """
        Return str.

        :return:
        """
        price = self.calculate_price() / 100
        return f'{self.name.capitalize()} pizza with a price of {price}'


class Pizzeria:
    """Pizzeria."""

    def __init__(self, name: str, is_fancy: bool, budget: int):
        """
        Initialize pizzeria.

        :param name:
        :param is_fancy:
        :param budget:
        """
        self.name = name
        self.is_fancy = is_fancy
        self.budget = budget
        self.chef = []
        self.menu = []
        self.baked = []

    def add_chef(self, chef: Chef) -> Chef or None:
        """
        Add chef.

        :param chef:
        :return:
        """
        if self.is_fancy is True and chef.experience_level > 24 and (chef not in self.chef):
            self.chef.append(chef)
            return chef
        elif self.is_fancy is False and (chef not in self.chef):
            self.chef.append(chef)
            return chef
        return None

    def remove_chef(self, chef: Chef):
        """
        Remove chef.

        :param chef:
        :return:
        """
        if chef in self.chef:
            self.chef.remove(chef)

    def add_pizza_to_menu(self, pizza: Pizza):
        """
        Add pizza to menu.

        :param pizza:
        :return:
        """
        if pizza.calculate_price() <= self.budget:
            if pizza not in self.menu:
                if len(self.chef) > 0:
                    self.menu.append(pizza)

    def remove_pizza_from_menu(self, pizza: Pizza):
        """
        Remove pizza from menu.

        :param pizza:
        :return:
        """
        if pizza in self.menu:
            self.menu.remove(pizza)

    def bake_pizza(self, pizza: Pizza) -> Pizza or None:
        """
        Bake pizza.

        :param pizza:
        :return:
        """
        best = []
        for chef in self.chef:
            if chef.experience_level >= pizza.calculate_complexity():
                best.append(chef)
        if (pizza in self.menu) and (len(best) > 0):
            best.sort(key=lambda chef: chef.experience_level)
            best[0].experience_level += len(pizza.name) // 2
            tulu = pizza.calculate_price() * 4 + len(pizza.name) // 2
            best[0].money += (tulu // 2)
            self.budget += (tulu // 2)
            self.baked.append(pizza)
            return pizza
        return None

    def get_pizza_menu(self) -> list:
        """
        Get pizza menu.

        :return:
        """
        self.menu.sort(key=lambda p: p.calculate_price(), reverse=True)
        return self.menu

    def get_baked_pizzas(self) -> dict:
        """
        Get baked pizza.

        :return:
        """
        pizza_dict = {}
        for pizza in self.baked:
            if pizza not in pizza_dict:
                pizza_dict[pizza] = self.baked.count(pizza)
        return pizza_dict

    def get_chefs(self) -> list:
        """
        Get chefs.

        :return:
        """
        che = []
        if len(self.chef) > 0:
            for chef in self.chef:
                che.append(chef)
        che.sort(key=lambda chef: chef.experience_level)
        return che

    def __repr__(self):
        """
        Pizzeria.

        :return:
        """
        return f'{self.name.capitalize()} with {len(self.chef)} pizza chef(s).'


if __name__ == '__main__':
    pizzeria1 = Pizzeria("Mama's Pizza", True, 10000)
    print(pizzeria1)  # Mama's pizza with 0 pizza chef(s).

    pizzeria1.add_chef(Chef("Clara", 24))
    print(pizzeria1)
    # Mama's pizza with 0 pizza chef(s). -> Clara was not added because of low XP (24) since it's a fancy pizzeria.

    pizza1 = Pizza("basic", 20, ["Cheese", "Ham"])
    print(pizzeria1.bake_pizza(pizza1))  # None -> No such pizza on the menu nor a chef in the pizzeria.

    ##########################################################
    sebastian = Chef("Sebastian", 58)
    charles = Chef("Charles", 35)
    kimi = Chef("Kimi", 83)

    pizzeria1.add_chef(sebastian)
    pizzeria1.add_chef(charles)
    pizzeria1.add_chef(kimi)

    # Trying to order a pizza which is not on the menu.

    print(pizzeria1.bake_pizza(pizza1))  # None

    pizzeria1.add_pizza_to_menu(pizza1)  # Price is 8.85

    print(pizzeria1.budget)  # 9115
    print(pizzeria1.get_pizza_menu())  # [Basic pizza with a price of 8.85]

    print(pizzeria1.bake_pizza(pizza1))  # Basic pizza with a price of 8.85

    print(pizzeria1.get_chefs())
    # Charles was chosen to bake the pizza, because Charles' XP was the closest to pizza's complexity

    print(pizzeria1.budget)  # 10887
    print(charles.money)  # 1772

    print(pizzeria1.get_baked_pizzas())  # {Basic pizza with a price of 8.85: 1}

    print("##########################################################")
    pizzeria2 = Pizzeria("Maranello", False, 10000)

    fernando = Chef("Fernando", 9)
    felipe = Chef("Felipe", 6)
    michael = Chef("Michael", 17)
    rubens = Chef("Rubens", 4)
    eddie = Chef("Eddie", 5)

    pizzeria2.add_chef(fernando)
    pizzeria2.add_chef(felipe)
    pizzeria2.add_chef(michael)
    pizzeria2.add_chef(rubens)
    pizzeria2.add_chef(eddie)

    margherita = Pizza("Margherita", 20, ["Sauce", "Mozzarella", "Basil"])
    smoke = Pizza("Big Smoke", 30, ["nine", "NINE", "six w/dip", "seven", "45", "45 w/cheese", "SODA"])

    pizzeria2.add_pizza_to_menu(margherita)
    pizzeria2.add_pizza_to_menu(smoke)

    print(pizzeria2.get_pizza_menu())  # [Big smoke pizza with a price of 20.67, Margherita pizza with a price of 8.85]
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Eddie with 5 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(margherita)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Eddie with 10 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(smoke)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Eddie with 14 XP, Pizza chef Michael with 17 XP]
    print(Chef("Arnold", 58))
    print(Pizza("Pizzap", 20, ["Cheese", "Ham"]))
