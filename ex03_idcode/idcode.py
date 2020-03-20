# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if year_number > 99:
        return False
    else:
        return True


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if 12 >= month_number >= 1:
        return True
    else:
        return False


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if gender number is correct.

    :param gender_number: int
    :return: boolean
    """
    if gender_number > 6:
        return False
    if gender_number == 0:
        return False
    else:
        return True


def is_leap_year(year: int) -> bool:
    """
    Check if year number is a leap year.

    :param year: int
    :return: boolean
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def get_gender(gender_number: int):
    """
    Check gender number for sex.

    :param gender_number: int
    :return: male or female
    """
    if gender_number == 2 or gender_number == 4 or gender_number == 6:
        return "female"
    if gender_number == 1 or gender_number == 3 or gender_number == 5:
        return "male"
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    if month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11 and day_number > 30:
        return False
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12 and day_number > 31:
        return False
    if month_number > 12 or month_number == 0:
        return False
    if month_number == 2 and day_number == 29:
        year = is_leap_year(year_number)
        if year is True:
            return True
        elif year is False:
            return False
    if month_number == 2 and day_number > 29:
        return False
    if day_number > 31:
        return False
    else:
        return True


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if 0 < birth_number <= 999:
        return True
    else:
        return False


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    check_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    check_sum = 0
    for i in range(10):
        check_sum += int(id_code[i]) * check_numbers[i]
        if check_sum == 10:
            for a in range(10):
                check_ten = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                check_sum += int(id_code[a]) * check_ten[a]
    last = int(id_code[10])
    lastlast = check_sum % 11
    if last == lastlast:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    if gender_number == 1 or gender_number == 2:
        year18 = 1800 + int(year_number)
        return year18
    if gender_number == 3 or gender_number == 4:
        year19 = 1900 + int(year_number)
        return year19
    if gender_number == 5 or gender_number == 6:
        year20 = 2000 + int(year_number)
        return year20


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    if 1 <= birth_number <= 999:
        dict_birth = {
            range(1, 11): "Kuressaare",
            range(11, 21): "Tartu",
            range(21, 221): "Tallinn",
            range(221, 271): "Kohtla-Järve",
            range(271, 371): "Tartu",
            range(371, 421): "Narva",
            range(421, 471): "Pärnu",
            range(471, 491): "Tallinn",
            range(491, 521): "Paide",
            range(521, 571): "Rakvere",
            range(571, 601): "Valga",
            range(601, 651): "Viljandi",
            range(651, 711): "Võru",
            range(710, 1000): "undefined"
        }
        for key in dict_birth:
            if birth_number in key:
                return dict_birth[key]
    else:
        return "Wrong input!"


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    id = int(id_code)
    idstr = list(id_code.split(""))
    gender = get_gender(id[0])
    day = idstr[5: 7]
    month = idstr[3: 5]
    year = idstr[1: 3]
    location = get_birth_place(id[7: 10])
    return f"This is a {gender} born on {day}.{month}.{year} in {location}"


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    idg = is_valid_control_number(id_code)
    if len(str(id_code)) == 11 and idg is True and int(id_code):
        return True
    else:
        return False
