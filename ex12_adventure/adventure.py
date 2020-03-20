"""Adventure."""
from math import floor


class Adventurer:
    """Adventurer."""

    def __init__(self, name: str, class_type, power):
        """
        Class adventure.

        :param name:
        :param class_type:
        :param power:
        """
        self.name = name
        self.power = power
        self.experience = 0
        if class_type in ["Fighter", "Druid", "Wizard", "Paladin"]:
            self.class_type = class_type
        else:
            self.class_type = "Fighter"

    def add_power(self, power):
        """Add power."""
        self.power += power

    def add_experience(self, exp):
        """Add experience."""
        self.experience += exp

    def __repr__(self):
        """Adventure repr."""
        return f'{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}.'


class Monster:
    """Monster."""

    def __init__(self, name: str, mon_type, power):
        """
        Class monster.

        :param name:
        :param mon_type:
        :param power:
        """
        self.mon_type = mon_type
        self.power = power
        if mon_type == 'Zombie':
            self.name = "Undead " + name
        else:
            self.name = name

    def __repr__(self):
        """Monster repr."""
        return f"{self.name} of type {self.mon_type}, Power: {self.power}."


class World:
    """World."""

    def __init__(self, PM):
        """World init."""
        self.adventurerlist = []
        self.monsterlist = []
        self.graveyard = []
        self.PM = PM
        self.active_adventurerlist = []
        self.active_monsterlist = []

    def get_monsterlist(self):
        """Get monsterlist."""
        monster = self.monsterlist
        for person in self.active_monsterlist:
            if person in self.monsterlist:
                monster.remove(person)
        return monster

    def get_adventurerlist(self):
        """Get adventurerlist."""
        adventurer = self.adventurerlist
        for person in self.active_adventurerlist:
            if person in self.adventurerlist:
                adventurer.remove(person)
        return adventurer

    def add_adventurer(self, adventurer: Adventurer):
        """Add adventurer."""
        if isinstance(adventurer, Adventurer):
            return self.adventurerlist.append(adventurer)

    def add_monster(self, monster: Monster):
        """Add monster."""
        if isinstance(monster, Monster):
            return self.monsterlist.append(monster)

    def get_graveyard(self):
        """Get graveyard."""
        return self.graveyard

    def get_python_master(self):
        """Get Python Master."""
        return self.PM

    def change_necromancer(self, boole):
        """Change necromancer."""
        if boole is True:
            self.revive_graveyard()
        elif boole is False:
            pass

    def revive_graveyard(self):
        """Revive graveyard."""
        for person in self.graveyard:
            if isinstance(person, Adventurer):
                monster = Monster("Undead " + person.name, "Zombie " + person.class_type, person.power)
                self.graveyard.remove(person)
                self.active_monsterlist.append(monster)
            else:
                monster = Monster(person.name, "Zombie", person.power)
                self.graveyard.remove(person)
                self.active_monsterlist.append(monster)

    def add_strongest(self, class_type):
        """Add strongest."""
        adventurers = []
        for person in self.adventurerlist:
            if person.class_type == class_type:
                adventurers.append(person)
        if len(adventurers) > 0:
            sorted_list = sorted(adventurers, key=lambda person: person.power, reverse=True)
            pretendent = sorted_list[0]
            self.adventurerlist.remove(pretendent)
            self.active_adventurerlist.append(pretendent)

    def add_weakest(self, class_type):
        """Add weakest."""
        adventurers = []
        for person in self.adventurerlist:
            if person.class_type == class_type:
                adventurers.append(person)
        if len(adventurers) > 0:
            sorted_list = sorted(adventurers, key=lambda person: person.power)
            pretendent = sorted_list[0]
            self.adventurerlist.remove(pretendent)
            self.active_adventurerlist.append(pretendent)

    def add_most_experience(self, class_type):
        """Add most experience."""
        adventurers = []
        for person in self.adventurerlist:
            if person.class_type == class_type:
                adventurers.append(person)
        if len(adventurers) > 0:
            adventurers.sort(key=lambda person: person.experience, reverse=True)
            self.adventurerlist.remove(adventurers[0])
            self.active_adventurerlist.append(adventurers[0])

    def add_least_experience(self, class_type):
        """Add least experience."""
        adventurers = []
        for person in self.adventurerlist:
            if person.class_type == class_type:
                adventurers.append(person)
        if len(adventurers) > 0:
            adventurers.sort(key=lambda person: person.experience)
            self.adventurerlist.remove(adventurers[0])
            self.active_adventurerlist.append(adventurers[0])

    def add_by_name(self, name):
        """Add by name."""
        for person in self.adventurerlist:
            if person.name == name:
                self.adventurerlist.remove(person)
                self.active_adventurerlist.append(person)

    def add_all_of_class_type(self, class_type):
        """Add all of class typee."""
        for person in self.adventurerlist:
            if person.class_type == class_type:
                self.adventurerlist.remove(person)
                self.active_adventurerlist.append(person)

    def add_all(self):
        """Add all."""
        self.active_adventurerlist.extend(self.adventurerlist)
        self.adventurerlist.clear()

    def get_active_adventurers(self):
        """Get active adventurers."""
        if len(self.active_adventurerlist) > 0:
            sorted_list = sorted(self.active_adventurerlist, key=lambda person: person.power)
            return sorted_list

    def add_monster_by_name(self, name):
        """Add monster by mane."""
        for person in self.monsterlist:
            if person.name == name:
                self.monsterlist.remove(person)
                self.active_monsterlist.append(person)

    def add_strongest_monster(self):
        """Add strongest."""
        sorted_list = sorted(self.monsterlist, key=lambda person: person.power, reverse=True)
        pretendent = sorted_list[0]
        if len(sorted_list) > 0:
            self.monsterlist.remove(pretendent)
            self.active_monsterlist.append(pretendent)

    def add_weakest_monster(self):
        """Add weakest monster."""
        sorted_list = sorted(self.monsterlist, key=lambda person: person.power)
        pretendent = sorted_list[0]
        if len(sorted_list) > 0:
            self.monsterlist.remove(pretendent)
            self.active_monsterlist.append(pretendent)

    def add_all_of_type(self, mon_type):
        """Add all type."""
        for person in self.adventurerlist:
            if person.mon_type == mon_type:
                self.monsterlist.remove(person)
                self.active_monsterlist.append(person)

    def add_all_monsters(self):
        """Add all monsters."""
        self.active_monsterlist.extend(self.monsterlist)
        self.monsterlist.clear()

    def get_active_monsters(self):
        """Get active monsters."""
        if len(self.active_monsterlist) > 0:
            self.active_monsterlist.sort(key=lambda p: p.power, reverse=True)
        return self.active_monsterlist

    def remove_character(self, name):
        """Remove character."""
        for person in self.monsterlist:
            if person.name == name:
                self.monsterlist.remove(person)
                return None
        for person in self.adventurerlist:
            if person.name == name:
                self.adventurerlist.remove(person)
                return None
        for person in self.graveyard:
            if person.name == name:
                self.graveyard.remove(person)
                return None

    def paladin_and_zombie(self):
        """Paladin."""
        is_paladin = 0
        is_zombie = 0
        power = 0

        for paladin in self.active_adventurerlist:
            if paladin.class_type == "Paladin":
                is_paladin += paladin.power

        for zombie in self.active_monsterlist:
            if zombie.mon_type in ["Zombie", "Zombie Fighter", "Zombie Druid", "Zombie Paladin", "Zombie Wizard"]:
                is_zombie += 1

        if is_paladin > 0 and is_zombie > 0:
            for person in self.active_adventurerlist:
                if person.class_type == "Paladin":
                    power += person.power
        return int(power)

    def druid_and_animal(self):
        """Druid."""
        is_druid = 0
        is_animal = 0
        power = 0

        for druid in self.active_adventurerlist:
            if druid.class_type == "Druid":
                is_druid += 1

        for animal in self.active_monsterlist:
            if animal.mon_type in ["Animal", "Ent"]:
                is_animal += 1

        if is_druid > 0 and is_animal > 0:
            for person in self.active_monsterlist:
                if person.mon_type in ["Animal", "Ent"]:
                    self.active_monsterlist.remove(person)
                    self.monsterlist.append(person)
                    power += person.power
        return int(power)

    def go_adventure(self, deadly=False):
        """Go adventure."""
        druid_bonus = self.druid_and_animal()  # отнять
        paladin_bonus = int(self.paladin_and_zombie())  # добавить

        advenurers_total_power = 0
        monsters_total_power = 0

        advenurers_total_power += paladin_bonus
        monsters_total_power -= druid_bonus

        for person in self.active_adventurerlist:
            advenurers_total_power += person.power

        for person in self.active_monsterlist:
            monsters_total_power += person.power

        if deadly is True:
            self.shituation_true(deadly, advenurers_total_power, monsters_total_power)
        if deadly is False:
            self.shituation_false(deadly, advenurers_total_power, monsters_total_power)

    def shituation_true(self, deadly, advenurers_total_power, monsters_total_power):
        """True."""
        if deadly is True:
            if advenurers_total_power > monsters_total_power:
                self.adventurers_win(monsters_total_power, deadly)

            if monsters_total_power > advenurers_total_power:
                for person in self.active_adventurerlist:
                    self.graveyard.append(person)
                    self.active_adventurerlist.remove(person)
                for person in self.active_monsterlist:
                    self.monsterlist.append(person)
                    self.active_monsterlist.remove(person)

            if monsters_total_power == advenurers_total_power:
                self.adventurers_draw()

    def adventurers_win(self, monsters_total_power, deadly):
        """Win."""
        adventurers = 0
        for person in self.active_adventurerlist:
            self.adventurerlist.append(person)
            adventurers += 1

        for person in self.active_monsterlist:
            self.active_monsterlist.remove(person)
            self.graveyard.append(person)

        bonus = floor(monsters_total_power / adventurers)

        for person in self.active_adventurerlist:
            if deadly is True:
                person.experience += bonus * 2
            if deadly is False:
                person.experience += bonus
            self.active_adventurerlist.remove(person)

    def adventurers_draw(self):
        """Draw."""
        for person in self.active_adventurerlist:
            power = person.power / 2
            person.experience += power
            self.active_adventurerlist.remove(person)
            self.adventurerlist.append(person)

        for person in self.active_monsterlist:
            self.active_monsterlist.remove(person)
            self.monsterlist.append(person)

    def shituation_false(self, deadly, advenurers_total_power, monsters_total_power):
        """False."""
        if deadly is False:
            if advenurers_total_power > monsters_total_power:
                self.adventurers_win(monsters_total_power, deadly)

            if monsters_total_power > advenurers_total_power:
                for person in self.active_adventurerlist:
                    self.active_adventurerlist.remove(person)
                    self.adventurerlist.append(person)
                for person in self.active_monsterlist:
                    self.active_monsterlist.remove(person)
                    self.monsterlist.append(person)

            if monsters_total_power == advenurers_total_power:
                self.adventurers_draw()


if __name__ == "__main__":
    print("Kord oli maailm.")
    Maailm = World("Sõber")
    print(Maailm.get_python_master())  # -> "Sõber"
    print(Maailm.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    Kangelane = Adventurer("Sander", "Paladin", 50)
    Tüütu_Sõber = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    Lahe_Sõber = Adventurer("Peep", "Druid", 25)
    Teine_Sõber = Adventurer("Toots", "Wizard", 40)

    print(Kangelane)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    print(Tüütu_Sõber)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 999999, Experience: 0."

    print("Sa ei tohiks kohe alguses ka nii tugev olla.")
    Tüütu_Sõber.add_power(-999959)
    print(Tüütu_Sõber)  # -> XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 40, Experience: 0.
    print()
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(Teine_Sõber)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()
    Lahe_Sõber.add_power(20)
    print("Sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 45, Experience: 0."

    Maailm.add_adventurer(Kangelane)
    Maailm.add_adventurer(Lahe_Sõber)
    Maailm.add_adventurer(Teine_Sõber)
    print(Maailm.get_adventurerlist())  # -> Sander, Peep ja Toots
    print('Olen siin')
    Maailm.add_monster(Tüütu_Sõber)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(Maailm.get_monsterlist())  # -> []
    Maailm.add_adventurer(Tüütu_Sõber)

    print()
    print()
    print("Oodake veidikene, ma tekitan natukene kolle.")
    Zombie = Monster("Rat", "Zombie", 10)
    GoblinSpear = Monster("Goblin Spearman", "Goblin", 10)
    GoblinArc = Monster("Goblin Archer", "Goblin", 5)
    BigOgre = Monster("Big Ogre", "Ogre", 120)
    GargantuanBadger = Monster("Massive Badger", "Animal", 1590)

    print(BigOgre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(Zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    Maailm.add_monster(GoblinSpear)

    print()
    print()
    print("Mängime esimese kakluse läbi!")
    Maailm.add_strongest("Druid")
    Maailm.add_strongest_monster()
    print(Maailm.get_active_adventurers())  # -> Peep
    print(Maailm.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]

    Maailm.go_adventure(True)

    Maailm.add_strongest("Druid")
    print(Maailm.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(Maailm.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]

    Maailm.add_monster(GargantuanBadger)
    Maailm.add_strongest_monster()

    Maailm.go_adventure(True)

    # Druid on loomade sõber, ja ajab massiivse mägra ära.
    print(Maailm.get_adventurerlist())  # -> Kõik 4 mängijat.
    print(Maailm.get_monsterlist())  # -> [Massive Badger of type Animal, Power: 1590.]

    Maailm.remove_character("Massive Badger")
    print(Maailm.get_monsterlist())  # -> []

    print(
        "Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
