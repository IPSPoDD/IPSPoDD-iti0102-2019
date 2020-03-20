"""Magic."""


class Wand:
    """Class wand."""

    def __init__(self, wood_type, core, score, owner=None):
        """Init."""
        self.wood_type = wood_type
        self.core = core
        self.score = score
        self.owner = owner

    set_wood_type = property()

    @set_wood_type.setter
    def set_wood_type(self, wood_type):
        """Setter."""
        self.wood_type = wood_type

    set_core = property()

    @set_core.setter
    def set_core(self, core):
        """Setter."""
        self.core = core

    @staticmethod
    def controll(wand):
        """Controll wand."""
        if isinstance(wand, Wand):
            print("Тип класса палочки.")
            return True

        else:
            print("Не класс палочки.")
            raise MismatchError("The wand like that does not exist!")

    def __str__(self):
        """String."""
        return f"Wand type is: {self.wood_type}, core: {self.core}, score: {self.score} and owner is: {self.owner}"


class Wizard:
    """Class wizard."""

    def __init__(self, name, power, fight, wand=None):
        """Init."""
        self.name = name
        self.power = power
        self.fight = fight
        self.wand = wand

    def give_wand(self, wand):
        """Give wand."""
        self.wand = wand

    # Допилить
    def __repr__(self):
        """Return string."""
        return f"Wizard name is {self.name} and she/he have (or not) wand {self.wand}"


class WizardySchool:
    """Wizardi school."""

    def __init__(self, school_name, max_count):
        """Init."""
        self.school_name = school_name
        self.max_count = max_count
        self.wizards = []
        self.houses = []

    def find_wizard(self, name):  # Этот метод необязательный
        """Find wizard."""
        for wiz in range(len(self.wizards)):
            if self.wizards[wiz].name == name:
                return wiz
        return None  # Ещё подумать

    def add_wizard(self, wizard):
        """Add wizard."""
        if Wand.controll(wizard.wand) and self.max_count > len(self.wizards):
            self.wizards.append(wizard)

    def delete_wizard(self, wizard):
        """Delete wizard."""
        if wizard in self.wizards:
            self.wizards.remove(wizard)
        pass

    def add_house(self, house):
        """Add house."""
        self.houses.append(house)

    def delete_house(self, house):
        """Delete house."""
        self.houses.remove(house)

    def all_wizards(self):
        """Wizard list."""
        return self.wizards

    def all_house(self, house):
        """Wizard in house list."""
        wiz = []
        for w in self.wizards:
            if w == house:
                wiz.append(w)
            continue
        return wiz

    def house_statistic(self):
        """House statistic."""
        pass

    def power_sort(self):
        """Sort by power."""
        return sorted(self.wizards, key=lambda x: x.power)

    def fight_sort(self):
        """Sort by fight."""
        return sorted(self.wizards, key=lambda x: x.fight)

    def score_sort(self):
        """Sort by score."""
        return sorted(self.wizards, key=lambda x: x.wand.score)

    def punnishment(self, wizard):
        """Punnishment."""
        self.wizards.remove(wizard)

    def respect(self, wizard):
        """Kiitus."""
        for w in self.wizards:
            if w == wizard:
                w.power += 1

    def fight(self, w1, w2):
        """Fight."""
        w1.fight += 1
        w2.fight += 1
        if w1.power < w2.power:
            print("I'M IN")
            print(f"And the winner is {w2.name}")
            return f"And the winner is {w2.name}"
        elif w1.power > w2.power:
            print(f"And the winner is {w1.name}")
            return f"And the winner is {w1.name}"
        else:
            return "Draw."

    def __str__(self):
        """String."""
        return f"School name is {self.school_name}, there are {len(self.wizards)} students.\nStudents: {self.wizards}.\nSchool have {len(self.houses)} houses. \nHouses: {self.houses}"


class DurmstrangHouse(WizardySchool):
    """House."""

    def sum_power(self):
        """Sum of power."""
        su = 0
        for i in self.wizards:
            su += i.power
        return su

    def __str__(self):
        """String method."""
        return "Student live in DurmstrangHouse."


class BeauxbatonsHouse(WizardySchool):
    """House."""

    def sum_score(self):
        """Sum of score."""
        su = 0
        for i in self.wizards:
            su += i.fight
        return su

    def __str__(self):
        """String method."""
        return "Student live in BeauxbatonsHouse."


class MismatchError(Exception):  # Как правильно оформить исключение?
    """Custom exception thrown when the fight lasts longer than 100 rounds."""

    pass


if __name__ == '__main__':
    print("\n================")

    print("\nПроверка класса Wand.")
    wa = Wand("Oak", "Cedar", 100, "Peeter")
    print(wa)

    print("\nДобралась до @property, смена дерева.")
    wa.set_wood_type = "Someone"  # Как добраться до метода @property. На крайний случай записать всне клвсса.
    print(wa)

    wa.set_core = 'Other'
    print(wa)

    oak = Wand("Tree", "Puu", 101, "Someone")

    print("\nДобралась до @staticmethod, проверка волшебной палочки на класс")
    print(wa.controll(wa))  # True
    try:
        print(wa.controll("Wand"))  # False. Исправить raise, выкидывает ошибку
    except MismatchError as error:
        print(error)
        if str(error) == "The wand like that does not exist!":
            print("-> MismatchError is correct")
        else:

            print("-> MismatchError's text is incorrect")

    print("\n================")

    print("\nПроверка класса Wizard.")

    wizard = Wizard("Harry", 100, 6)
    print(wizard)

    germiona = Wizard("Germoina", 110, 8)

    print("\nДаём палочку.")
    wizard.give_wand(wa)
    print(wizard)

    germiona.give_wand(oak)
    print(germiona)

    print("\n================")

    print("\nПроверка класса WizardySchool.")
    ws = WizardySchool("Unknown", 3)
    print(ws)

    print("\nДобавляем Wizard.")
    ws.add_wizard(wizard)
    ws.add_wizard(wizard)
    ws.add_wizard(germiona)
    print(ws)

    print("\nУдаляем Wizard.")
    ws.delete_wizard(wizard)
    print(ws)  # Студенты нечитабельны

    print("\nВыводим список Wizard.")
    print(ws.all_wizards())

    print("\nВыводим список House.")
    dh = DurmstrangHouse('DurmstrangHouse', 5)
    bh = BeauxbatonsHouse("BeauxbatonsHouse", 7)
    ws.add_house(dh)
    ws.add_house(bh)
    print(ws.houses)

    print("\nFight.")
    ws.fight(wizard, germiona)

    print("\n================")

    print("\nПроверка класса House.")
    dh = DurmstrangHouse('DurmstrangHouse', 5)
    dh.add_wizard(wizard)
    dh.add_wizard(wizard)
    print(dh.sum_power())

    bh = BeauxbatonsHouse("BeauxbatonsHouse", 7)
    bh.add_wizard(germiona)
    print(bh.sum_score())
