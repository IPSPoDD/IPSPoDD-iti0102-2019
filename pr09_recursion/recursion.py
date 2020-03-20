"""Recursion is recursion."""


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    recursive_reverse("") => ""
    recursive_reverse("abc") => "cba"

    :param s: string
    :return: reverse of s
    """
    if s:
        return s[-1] + recursive_reverse(s[0:-1])
    return ""


def remove_nums_and_reverse(string):
    """
    Recursively remove all the numbers in the string and return reversed version of that string without numbers.

    print(remove_nums_and_reverse("poo"))  # "oop"
    print(remove_nums_and_reverse("3129047284"))  # empty string
    print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5oh565ty7p4"))  # "python for life"
    print(remove_nums_and_reverse("  k 4"))  # " k  "

    :param string: given string to change
    :return: reverse version of the original string, only missing numbers
    """
    nums = set("0123456789")
    if string:
        if string[-1] not in nums:
            return string[-1] + remove_nums_and_reverse(string[:-1])
        return remove_nums_and_reverse(string[:-1])
    return ""


def task1(string):
    """
    Figure out what this code is supposed to do and rewrite it using recursion.

    :param string: given string
    :return: figure it out
    """
    if string:
        if string[0] == string[-1]:
            return task1(string[1:-1])
        return False
    return True


def task2(string):
    """
    Figure out what this code is supposed to do and rewrite it using iteration.

    :param string: given string
    :return: figure it out
    """
    if string == "":
        return ""
    word = ""
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            word += string[i] + "-"
        else:
            word += string[i]
    word += string[-1]
    return word
