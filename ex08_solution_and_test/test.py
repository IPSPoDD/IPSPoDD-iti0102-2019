"""Test."""
from solution import students_study
from solution import lottery
from solution import fruit_order
# import random


def test_students_study_5_18():
    """
    Test coffee.

    :return:
    """
    for num in range(5, 18):
        assert students_study(num, False) is False
        assert students_study(num, True) is True


def test_students_study_18_25():
    """
    Test coffee.

    :return:
    """
    for num in range(18, 25):
        assert students_study(num, False) is True
        assert students_study(num, True) is True


def test_students_study_1_5():
    """
    Test coffee.

    :return:
    """
    for num in range(1, 5):
        assert students_study(num, False) is False
        assert students_study(num, True) is False


def test_students_study_false():
    """
    Test coffee.

    :return:
    """
    assert students_study(0, True) is False
    assert students_study(25, False) is False


def test_lottery():
    """
    Test lottery.

    :return:
    """
    assert lottery(5, 5, 5) == 10
    assert lottery(2, 3, 1) == 1
    assert lottery(1, 2, 3) == 1
    assert lottery(-1, -2, -3) == 1
    assert lottery(10, 56, -9) == 1
    assert lottery(99, 98, 97) == 1
    assert lottery(9999, 9998, 9997) == 1


def test_lottery_same():
    """
    Test lottery.

    :return:
    """
    for num in range(6, 100000):
        assert lottery(num, num, num) == 5
    for num in range(-100000, 5):
        assert lottery(num, num, num) == 5


def test_lottery_different():
    """
    Test lottery.

    :return:
    """
    for num in range(-100000, 100000):
        assert lottery(num, num, not num) == 0
        assert lottery(num, not num, num) == 0
        assert lottery(num, not num, not num) == 1


def test_fruit_order():
    """
    Test fruit.

    :return:
    """
    assert fruit_order(4, 1, 9) == 4
    assert fruit_order(6, 2, 5) == 0
    assert fruit_order(23, 2, 10) == 0
    assert fruit_order(23, 0, 10) == 10
    assert fruit_order(5, 1, 8) == 3
    assert fruit_order(5, 2, 5) == 0


def test_fruit_order_false():
    """
    Test fruit.

    :return:
    """
    assert fruit_order(1, 2, 3) == -1
    assert fruit_order(3, 1, 4) == -1
    assert fruit_order(6, 2, 26) == -1
    assert fruit_order(1, 100, 19) == -1
    assert fruit_order(3, 1, 10) == -1


def test_fruit_order_same():
    """
    Test fruit.

    :return:
    """
    for num in range(0, 5):
        assert fruit_order(num, num, num) == num
        assert fruit_order(num, 1 + num, num) == num
        assert fruit_order(num + 2, 1 + num, num) == num
        assert fruit_order(num + 1, num + 1, num) == num


def test_fruit_order_zero():
    """
    Test fruit.

    :return:
    """
    for num in range(10000):
        assert fruit_order(num, num, 0) == 0
        assert fruit_order(num, 0, num) == num
        assert fruit_order(0, num, 0) == 0
        assert fruit_order(num, 0, 0) == 0
        assert fruit_order(num, 0, num + 1) == -1
        assert fruit_order(num + 1, 0, num) == num


def test_fruit_order_middle():
    """
    Test fruit.

    :return:
    """
    for num in range(10000):
        if num % 5 == 0:
            assert fruit_order(0, num, num) == 0
            g = num // 5
            assert fruit_order(0, g, num) == 0
            assert fruit_order(0, g, num + 1) == -1
            assert fruit_order(0, g, num + 5) == -1
            assert fruit_order(0, g, num - 1) == -1
            assert fruit_order(num, g, num) == 0
        if num % 5 > 1:
            assert fruit_order(1, num, num) == -1  # Больше не надо
        if num // 5 > 1:
            k = num % 5
            assert fruit_order(num, num, num) == k
            assert fruit_order(k - 1, num, num) == -1
            v = num * 5 + num + 1
            assert fruit_order(num, num, v) == -1


def test_fruit_order_last():
    """
    Test fruit.

    :return:
    """
    for num in range(10000):
        d = num // 5
        n = num % 5
        assert fruit_order(n, d, num + 1) == -1
        assert fruit_order(n - 1, d, num + 1) == -1
        assert fruit_order(n, d - 1, num + 1) == -1
        assert fruit_order(0, d, num + 1) == -1
        assert fruit_order(0, 0, num + 1) == -1
        if num != 0:
            assert fruit_order(0, 0, num) == -1
