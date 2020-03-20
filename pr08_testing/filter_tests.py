"""Testing."""
import random
from filter import sort_list
from filter import longest_filtered_word
from filter import remove_vowels


def test_remove_vowels_when_no_vowels():
    """
    Check for vowels.

    :return:
    """
    assert remove_vowels("hello") == ("hll")
    assert remove_vowels("BrtGhFtrW") == ("BrtGhFtrW")
    assert remove_vowels("Vrtttt") == ("Vrtttt")
    assert remove_vowels("Re") == ("R")
    assert remove_vowels("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~)") == ("0123456789bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~)")


def test_remove_vowels_when_no_vowels_empty():
    """
    Check for vowels.

    :return:
    """
    assert remove_vowels("") == ""


def test_remove_vowels_when_no_vowels_vow():
    """
    Check for vowels.

    :return:
    """
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in vowel:
        assert remove_vowels(char) == ("")
    assert remove_vowels("AEIOUaeiuo") == ("")


def test_longest_filtered_word_when_long():
    """
    Check for long world without vowel.

    :return:
    """
    assert longest_filtered_word(["Bunny", "Tiger", "Bear", "Snake"]) == ("Bnny")
    assert longest_filtered_word(["Tiger", "Bear", "Snake"]) == ("Tgr")
    assert longest_filtered_word(["Snake", "Tiger", "Bear"]) == ("Snk")
    assert longest_filtered_word(["Tiger", "Bear", "Snake", "Bunny"]) == ("Bnny")


def test_longest_filtered_word_when_long_short():
    """
    Check for long world without vowel.

    :return:
    """
    assert longest_filtered_word(["Red"]) == ("Rd")
    assert longest_filtered_word(["Hahaaaa"]) == ("Hh")


def test_longest_filtered_word_when_long_repeat():
    """
    Check for long world without vowel.

    :return:
    """
    assert longest_filtered_word(["Red", "Red", "Red", "Red", "Red"]) == ("Rd")


def test_longest_filtered_word_when_long_empty():
    """
    Check for long world without vowel.

    :return:
    """
    assert longest_filtered_word([""]) == ("")
    assert longest_filtered_word([]) is None
    assert longest_filtered_word(["", "", ""]) == ""


def test_sort_list():
    """
    Check for sorted list by length.

    :return:
    """
    assert sort_list(["Bunny", "Tiger", "Bear", "Snake"]) == (['Bnny', 'Tgr', 'Snk', 'Br'])
    assert sort_list(["Red"]) == (["Rd"])


def test_sort_list_empty():
    """
    Check for sorted list by length.

    :return:
    """
    assert sort_list([]) == []
    assert sort_list("") == []
    assert sort_list([""]) == ([""])


def test_random():
    """
    Check for random.

    :return:
    """
    random_string_vowel = "".join(random.choices("aeiou"))
    for char in random_string_vowel:
        assert remove_vowels(char) == ("")
