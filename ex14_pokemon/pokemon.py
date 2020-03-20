"""Pokemon."""
import requests
import json
import os


# def say(text):
#     """Say."""
#     print('->', text)
#     pass


def choose_which_pokemon_hits_first_v2(pokemon1, pokemon2):
    """Second."""
    if len(pokemon1.data["abilities"]) > len(pokemon2.data["abilities"]):
        return pokemon1, pokemon2
    elif len(pokemon2.data["abilities"]) > len(pokemon1.data["abilities"]):
        return pokemon2, pokemon1
    else:
        if len(pokemon1.data["moves"]) > len(pokemon2.data["moves"]):
            return pokemon1, pokemon2
        elif len(pokemon2.data["moves"]) > len(pokemon1.data["moves"]):
            return pokemon2, pokemon1
        else:
            if pokemon1.data["base_experience"] > pokemon2.data["base_experience"]:
                return pokemon1, pokemon2
            elif pokemon2.data["base_experience"] > pokemon1.data["base_experience"]:
                return pokemon2, pokemon1


class World:
    """World class."""

    def __init__(self, name, offset, limit):
        """
        Class constructor.

        :param name: name of the pokemon world
        :param offset: offset for api request
        :param limit: limit for api request
        Check if f"{name}_{offset}_{limit}.txt" file exists, if it does, read pokemons in from that file, if not, then make an api
        request to f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}" to get pokemons and dump them to
        f"{name}_{offset}_{limit}.txt" file
        """
        self.pokemons = []
        pokemony = requests.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}")
        self.name = name
        self.offset = offset
        self.limit = limit

        if os.path.exists(f"{name}_{offset}_{limit}.txt"):
            f = open(f"{name}_{offset}_{limit}.txt", "r")

            # spisok_pokemonov = list(f)[0][1:-1].split(',')

            for pokemon in f:
                p = Pokemon(pokemon)  # Поменяно
                self.pokemons.append(p)

            # self.pokemons = json.load(f)

            f.close()
        else:
            for pokemon in pokemony.json()['results']:
                url = pokemon["url"]
                p = Pokemon(url)  # Поменяно
                self.pokemons.append(p)
            self.dump_pokemons_to_file_as_json(f"{name}_{offset}_{limit}.txt")

    def dump_pokemons_to_file_as_json(self, name):
        """
        Write all self.pokemons separated by a newline to the given filename(if it doesnt exist, then create one).

        :param name: name of the .txt file
        PS: Write the pokemon.__str__() version, not __repr__() as only name is useless :)
        """
        with open(name, 'w') as f:  # Changed!
            for p in self.pokemons:
                f.write(json.dumps(p) + '\n')
            # f.close()

    def fight(self):
        """
        A wild brawl between all pokemons where points are assigned to winners.

        Note, every pokemon fights another pokemon only once
        Fight lasts until one pokemon runs out of hp.
        every pokemon hits only 1 time per turn and they take turns when they attack.
        Call choose_which_pokemon_hits_first(pokemon1, pokemon2): to determine which pokemon hits first
        Call pokemon_duel function in this method with the aforementioned pokemons.
        every exception thrown by called sub methods must be caught and dealt with.
        """
        index = 0
        for pokemon_1 in self.pokemons:
            index += 1
            for i in range(index, len(self.pokemons)):
                pokemon_2 = self.pokemons[i]
                try:
                    pokemon1, pokemon2 = self.choose_which_pokemon_hits_first(pokemon_1, pokemon_2)
                    try:
                        self.pokemon_duel(pokemon1, pokemon2)
                    except PokemonFightResultsInATieException:
                        continue
                except SamePokemonFightException:
                    continue

    @staticmethod
    def pokemon_duel(pokemon1, pokemon2):
        """
        Here 2 pokemons fight.

        To get the attack and defense of the pokemon, call pokemon1.get_pokemon_attack()
        and pokemon1.get_pokemon_defense() respectively.
        Attack is multiplied by the pokemon1.get_attack_multiplier(list(second.data['types'])) multiplier
        Total attak is
        pokemon1.get_pokemon_attack(turn_counter) * multiplier1 - second.get_pokemon_defense(turn_counter)
        [turn counter starts from 1]
        Total attack is subtracted from other pokemons hp.
        Pokemons can not heal during the fight. (when total attack is negative, no damage is dealt)
        If the fight between 2 pokemons lasts more than 100 turns, then PokemonFightResultsInATieException() is thrown.
        If one pokemon runs out of hp, fight ends and the winner gets 1 point, (self.score += 1)
        then both pokemons are healed to full hp.

        :param pokemon1: pokemon, who attacks first.
        :param pokemon2: pokemon, who attacks second.
        :return winner: pokemon, who won.
        """
        pass

    @staticmethod
    def choose_which_pokemon_hits_first(pokemon1, pokemon2):
        """
        Pokemon who's speed is higher, goes first.

        If both pokemons have the same speed, then pokemon who's weight
        is lower goes first, if both pokemons have same weight, then pokemon who's height is lower goes first,
        if both pokemons have the same height, then the pokemon with more abilities goes first, if they have the same
        amount of abilities, then the pokemon with more moves goes first, if the pokemons have the same amount of
        moves, then the pokemon with higher base_experience goes first, if the pokemons have the same
        base_experience then SamePokemonFightException() is thrown.

        :param pokemon1:
        :param pokemon2:
        :return pokemon1 who goes first and pokemon2 who goes second (return pokemon1, pokemon2)
        """
        if pokemon1.data["speed"] == pokemon2.data["speed"] and pokemon1.data["weight"] == pokemon2.data["weight"] \
                and pokemon1.data["height"] == pokemon2.data["height"] \
                and len(pokemon1.data["abilities"]) == len(pokemon2.data["abilities"]) \
                and len(pokemon1.data["moves"]) == len(pokemon2.data["moves"]) \
                and pokemon1.data["base_experience"] == pokemon2.data["base_experience"]:
            raise SamePokemonFightException()
        if pokemon1.data["speed"] > pokemon2.data["speed"]:
            return pokemon1, pokemon2
        elif pokemon1.data["speed"] < pokemon2.data["speed"]:
            return pokemon2, pokemon1
        else:
            if pokemon1.data["weight"] < pokemon2.data["weight"]:
                return pokemon1, pokemon2
            elif pokemon2.data["weight"] < pokemon1.data["weight"]:
                return pokemon2, pokemon1
            else:
                if pokemon1.data["height"] < pokemon2.data["height"]:
                    return pokemon1, pokemon2
                elif pokemon2.data["height"] < pokemon1.data["height"]:
                    return pokemon2, pokemon1
                else:
                    return choose_which_pokemon_hits_first_v2(pokemon1, pokemon2)

    def get_leader_board(self):
        """
        Get Pokemons by given format in a list sorted by the pokemon.score.

        In case of the same score, order pokemons by their name (ascending).

        :return: List of leader board. where winners are first
        """
        leaders = sorted(self.pokemons, key=lambda x: x.data["name"])
        return sorted(leaders, key=lambda x: x.score, reverse=True)

    def get_pokemons_sorted_by_attribute(self, attribute: str):
        """
        Get Pokemons by given format in a  list sorted by the pokemon.data[attribute].

        :param attribute:  pokemon data attribute to sort by
        :return: sorted List of pokemons
        """
        return self.pokemons.sort(key=lambda x: x.data[attribute])


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, url_or_path_name: str):
        """
        Class constructor.

        :param url_or_path_name: url or json object.
        If it is url, then parse information from request to proper
        json file and save it to self.data.
        If it is a string representation of a json object, then parse it into json object and save to self.data
        """
        self.score = 0
        self.data = {}
        # if url_or_path_name[0] != '{':
        #     self.data = {}
        #     self.parse_json_to_pokemon_information(url_or_path_name)
        # else:
        #     self.data = json.loads(url_or_path_name)
        try:
            self.data = {}
            self.parse_json_to_pokemon_information(url_or_path_name)
        except Exception:
            self.data = json.loads(url_or_path_name)

    def parse_json_to_pokemon_information(self, url):
        """
        Called from constructor and this method requests data from url to parse it into proper json object.

        and then saved under self.data example done previously
        :param url: url where the information is requested.
        """
        # file = {}
        if url[:7] == 'http://' or url[:8] == 'https://':
            # say("If сработал, значит это URL")
            file = requests.get(url).json()
        else:
            # say("Зашли в else, значит это адрес на локалке")
            x = open(url)
            file = json.load(x)
            x.close()
            # say("Закрыли файл")
            # self.parse_json_to_pokemon_information(file)
        # say("Работаем с file " + file['name'])
        self.data['name'] = file['name']
        self.data['speed'] = file['stats'][0]['base_stat']
        self.data['attack'] = file['stats'][4]['base_stat']
        self.data['defence'] = file['stats'][3]['base_stat']
        self.data['special-attack'] = file['stats'][2]['base_stat']
        self.data['special-defence'] = file['stats'][1]['base_stat']
        self.data['hp'] = file['stats'][5]['base_stat']
        self.data['type'] = []
        for i in file['types']:
            self.data['type'].append(i['type']['name'])
        self.data['abilities'] = []
        for i in file['abilities']:
            self.data['abilities'].append(i['ability']['name'])
        self.data['forms'] = []
        for i in file['forms']:
            self.data['forms'].append(i['name'])
        self.data['moves'] = []
        for i in file['moves']:
            self.data['moves'].append(i['move']['name'])
        self.data['height'] = file['height']
        self.data['base_experience'] = file['base_experience']

    def get_attack_multiplier(self, other: list):
        """
        Calculate Pokemons attack multiplier against others types and take the best result.

        get the initial multiplier from Fighting Multiplier matrix.
        For example if self.type == ['fire'] and other == ['ground']: return fighting_multipliers['fire']['ground']
        if the defendant has dual types, then multiply the multipliers together.
        if the attacker has dual-types, then the best option is
        chosen(attack can only be of 1 type, choose better[higher multiplier])
        self.pokemon is attacking, other is defending.

        :param other: list of other pokemon2.data['types']
        :return: Multiplier.
        """
        fighting_multipliers = {
            'normal': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 0.5,
                       'bug': 1.0, 'ghost': 0.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0,
                       'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0},
            'fighting': {'normal': 2.0, 'fighting': 1.0, 'flying': 0.5, 'poison': 0.5, 'ground': 1.0, 'rock': 2.0,
                         'bug': 0.5, 'ghost': 0.0, 'steel': 2.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0,
                         'electric': 1.0, 'psychic': 0.5, 'ice': 2.0, 'dragon': 1.0, 'dark': 2.0, 'fairy': 0.5},
            'flying': {'normal': 1.0, 'fighting': 2.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 0.5,
                       'bug': 2.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 2.0, 'electric': 0.5,
                       'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0},
            'poison': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5,
                       'bug': 1.0, 'ghost': 0.5, 'steel': 0.0, 'fire': 1.0, 'water': 1.0, 'grass': 2.0, 'electric': 1.0,
                       'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 2.0},
            'ground': {'normal': 1.0, 'fighting': 1.0, 'flying': 0.0, 'poison': 2.0, 'ground': 1.0, 'rock': 2.0,
                       'bug': 0.5, 'ghost': 1.0, 'steel': 2.0, 'fire': 2.0, 'water': 1.0, 'grass': 0.5, 'electric': 2.0,
                       'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0},
            'rock': {'normal': 1.0, 'fighting': 0.5, 'flying': 2.0, 'poison': 1.0, 'ground': 0.5, 'rock': 1.0,
                     'bug': 2.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 2.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0,
                     'psychic': 1.0, 'ice': 2.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0},
            'bug': {'normal': 1.0, 'fighting': 0.5, 'flying': 0.5, 'poison': 0.5, 'ground': 1.0, 'rock': 1.0,
                    'bug': 1.0, 'ghost': 0.5, 'steel': 0.5, 'fire': 0.5, 'water': 1.0, 'grass': 2.0, 'electric': 1.0,
                    'psychic': 2.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 2.0, 'fairy': 0.5},
            'ghost': {'normal': 0.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 1.0,
                      'bug': 1.0, 'ghost': 2.0, 'steel': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0,
                      'psychic': 2.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 0.5, 'fairy': 1.0},
            'steel': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 2.0,
                      'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 1.0, 'electric': 0.5,
                      'psychic': 1.0, 'ice': 2.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 2.0},
            'fire': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 0.5,
                     'bug': 2.0, 'ghost': 1.0, 'steel': 2.0, 'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'electric': 1.0,
                     'psychic': 1.0, 'ice': 2.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0},
            'water': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 2.0, 'rock': 2.0,
                      'bug': 1.0, 'ghost': 1.0, 'steel': 1.0, 'fire': 2.0, 'water': 0.5, 'grass': 0.5, 'electric': 1.0,
                      'psychic': 1.0, 'ice': 1.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0},
            'grass': {'normal': 1.0, 'fighting': 1.0, 'flying': 0.5, 'poison': 0.5, 'ground': 2.0, 'rock': 2.0,
                      'bug': 0.5, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 2.0, 'grass': 0.5, 'electric': 1.0,
                      'psychic': 1.0, 'ice': 1.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0},
            'electric': {'normal': 1.0, 'fighting': 1.0, 'flying': 2.0, 'poison': 1.0, 'ground': 0.0, 'rock': 1.0,
                         'bug': 1.0, 'ghost': 1.0, 'steel': 1.0, 'fire': 1.0, 'water': 2.0, 'grass': 0.5,
                         'electric': 0.5, 'psychic': 1.0, 'ice': 1.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0},
            'psychic': {'normal': 1.0, 'fighting': 2.0, 'flying': 1.0, 'poison': 2.0, 'ground': 1.0, 'rock': 1.0,
                        'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 1.0,
                        'electric': 1.0, 'psychic': 0.5, 'ice': 1.0, 'dragon': 1.0, 'dark': 0.0, 'fairy': 1.0},
            'ice': {'normal': 1.0, 'fighting': 1.0, 'flying': 2.0, 'poison': 1.0, 'ground': 2.0, 'rock': 1.0,
                    'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'electric': 1.0,
                    'psychic': 1.0, 'ice': 0.5, 'dragon': 2.0, 'dark': 1.0, 'fairy': 1.0},
            'dragon': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 1.0,
                       'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0,
                       'psychic': 1.0, 'ice': 1.0, 'dragon': 2.0, 'dark': 1.0, 'fairy': 0.0},
            'dark': {'normal': 1.0, 'fighting': 0.5, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 1.0,
                     'bug': 1.0, 'ghost': 2.0, 'steel': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0,
                     'psychic': 2.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 0.5, 'fairy': 0.5},
            'fairy': {'normal': 1.0, 'fighting': 2.0, 'flying': 1.0, 'poison': 0.5, 'ground': 1.0, 'rock': 1.0,
                      'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 1.0, 'grass': 1.0, 'electric': 1.0,
                      'psychic': 1.0, 'ice': 1.0, 'dragon': 2.0, 'dark': 2.0, 'fairy': 1.0}}

        spisok = []  # Поле для ошибок

        for i in range(len(self.data['type'])):
            spisok.append([])
            for j in other:
                spisok[i] *= fighting_multipliers[self.data['type'][i]][j]

        return max(spisok)

    def get_pokemon_attack(self, turn_counter):
        """
        .

        :param turn_counter: every third round the attack is empowered. (return self.data['special-attack'])
        otherwise basic attack is returned (self.data['attack'])
        """
        if turn_counter % 3 == 0:
            return self.data['special-attack']
        else:
            return self.data['attack']

    def get_pokemon_defense(self, turn_counter):
        """
        Note: whatever the result is returned, return half of it instead (for example return self.data['defense'] / 2).

        :param turn_counter: every second round the defense is empowered. (return self.data['special-defense'])
        otherwise basic defense is returned (self.data['defense'])
        """
        if turn_counter % 2 == 0:
            return self.data['special-defense'] / 2
        else:
            return self.data['defense'] / 2

    def __str__(self):
        """
        String representation of json(self.data) object.

        One way to accomplish this is to use json.dumps functionality
        :return: string version of json file with necessary information
        """
        return json.dumps(self.data)

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name in string format and his score, for example: "garchomp-mega 892"
        """
        return f'{self.data["name"]} {self.score}'


class SamePokemonFightException(Exception):
    """Custom exception thrown when same pokemons are fighting."""

    pass


class PokemonFightResultsInATieException(Exception):
    """Custom exception thrown when the fight lasts longer than 100 rounds."""

    pass


if __name__ == "__main__":
    # say('src = 1.json')
    p = Pokemon("1.json")
    print(p.data['name'])
    # say('src = https://pokeapi.co/api/v2/pokemon/1/')
    p = Pokemon("https://pokeapi.co/api/v2/pokemon/1/")
    print(p.data['name'])
    print(p)
