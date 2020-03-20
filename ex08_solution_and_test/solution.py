"""Solution."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 18 <= time <= 24:
        return True
    if 5 <= time <= 17 and coffee_needed is True:
        return True
    if 1 <= time <= 4 and coffee_needed is False:
        return True
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    if a == b and b == c:
        return 5
    if a != b and b != c and a != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    summa = small_baskets + big_baskets * 5
    big = ordered_amount // 5
    small = ordered_amount % 5
    if ordered_amount == 0:
        return 0
    if ordered_amount > summa:
        return -1
    else:
        if big <= big_baskets:
            if small <= small_baskets:
                return small
            else:
                return -1
        if big > big_baskets:
            if ordered_amount - big < small_baskets:
                if small_baskets > ordered_amount:
                    return ordered_amount
            else:
                return -1
