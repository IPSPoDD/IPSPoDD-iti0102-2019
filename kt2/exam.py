"""KT2 (R10)."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) < 4:
        return s[::-1]
    else:
        new_s = s[-2] + s[-1] + s[2:-2] + s[:2]
        return new_s


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if 7 not in nums:
        return False
    increment = 0
    for i in nums:
        if i == 7:
            increment += + 1
        else:
            increment = increment
    if increment == 3:
        for i in range(len(nums) - 1):
            print(i)
            if nums[i] != nums[i + 1]:
                print(nums[i])
                return True
            else:
                return False
    else:
        return False


def g_happy(s):
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    if "g" not in s:
        return False
    else:
        for i in range(len(s)):
            if s[i] == "g":
                if "g" == s[i + 1]:
                    return True
                else:
                    return False
