"""Filtering."""


def remove_vowels(string: str) -> str:
    """
    Remove vowels (a, e, i, o, u).

    :param string: Input string
    :return string without vowels.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    chars = []
    for i in string:
        if i not in vowels:
            chars.append(i)
    return "".join(chars)  # соединение элементов через определенный символ.


def longest_filtered_word(string_list: list) -> str:
    """
    Filter, find and return the longest string.

    :param string_list: List of strings.
    :return: Longest string without vowels.
    """
    new_list = ""
    for i in string_list:
        if len(remove_vowels(i)) > len(new_list):
            new_list = remove_vowels(i)
    return new_list


def sort_list(string_list: list) -> list:
    """
    Filter vowels in strings and sort the list by the length.

    Longer strings come first.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of symbols in descending order.
    """
    sort_list = []
    for i in string_list:
        sort_list.append(remove_vowels(i))
    sort_sort = sorted(sort_list, key=len, reverse=True)
    return sort_sort


if __name__ == '__main__':
    # print(remove_vowels(""))  # => ""
    # print(remove_vowels("hello"))  # => "hll"
    # print(remove_vowels("Home"))  # => "Hm"
    # print(longest_filtered_word(["Red", "Bunny", "Tiger", "Bear", "Snake"]))  # => "Bnny"
    print(sort_list(["Bunny", "Tiger", "Bear", "Snake"]))  # => ['Bnny', 'Tgr', 'Snk', 'Br']
