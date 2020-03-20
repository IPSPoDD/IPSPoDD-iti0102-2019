"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '.
    Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    h = (base + 1) // 2
    return [stuff(i, h, base, char) for i in range(h)]


def stuff(i, h, base, char):
    """
    Blah.

    :param i:
    :param h:
    :param base:
    :param char:
    :return:
    """
    s = h - 1 - i
    k = base - 2 * s
    row = list(" " * s + char * k + " " * s)
    return row


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    a = pyramid_a[::-1]
    b = pyramid_b[::-1]
    pyramid = []
    if len(pyramid_a) == len(pyramid_b):
        for i in range(0, len(a)):
            v = a[i] + b[i]
            pyramid.append(v)

    if len(pyramid_a) > len(pyramid_b):
        digit = int(len(a)) - int(len(b))  # разница в высоте
        base = len(pyramid_b[0])  # ширина мелкого
        value = [" "] * base
        b.extend([value] * digit)
        for i in range(0, len(a)):
            v = a[i] + b[i]
            pyramid.append(v)
    if len(pyramid_b) > len(pyramid_a):
        digit = int(len(b)) - int(len(a))
        base = len(pyramid_a[0])
        value = [" "] * base
        a.extend([value] * digit)
        for i in range(0, len(a)):
            v = a[i] + b[i]
            pyramid.append(v)

    return [i for i in pyramid[::-1]]


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    pyr = "\n".join(["".join(i) for i in pyramid])
    return pyr


if __name__ == '__main__':
    pyramid_a = make_pyramid(3, "A")
    print(pyramid_a)  # ->
    """
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    """

    pyramid_b = make_pyramid(6, 'a')
    print(pyramid_b)  # ->
    """
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    joined = join_pyramids(pyramid_a, pyramid_b)
    print(joined)  # ->
    """
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    pyramid_string = to_string(joined)
    print(pyramid_string)  # ->
    """
         aa
     A  aaaa
    AAAaaaaaa
    """
