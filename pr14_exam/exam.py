"""Exam."""


def swap_items(dic: dict) -> dict:
    """
    Given a dictionary return a new dictionary where keys and values are swapped.

    If duplicate keys in the new dictionary exist, leave the first one.
    {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
    {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}

    :param dic: original dictionary
    :return: dictionary where keys and values are swapped
    """
    dictionary = {}
    for k, v in dic.items():
        if v not in dictionary:
            dictionary[v] = k
    return dictionary


def find_divisors(number) -> list:
    """
    The task is to find all the divisors for given number in range to the given number's value.

    Divisor - a number that divides evenly into another number.
    Return list of given number divisors in ascending order.
    NB! Numbers 1 and number itself must be excluded if there are more divisors
    than 1 and number itself!
    (138) > [2, 3, 6, 23, 46, 69]
    (3) > [1, 3]
    :param number: int
    :return: list of number divisors
    """
    numb = []
    for i in range(number + 1):
        if i > 0:
            if number % i == 0:
                numb.append(i)
        continue
    if len(numb) > 2:
        numb.remove(numb[0])
        numb.remove(numb[-1])
    return numb


def sum_of_multiplies(first_num, second_num, limit) -> int:
    """
    The task is to find all the multiplies of each given of two numbers within the limit.

    Then, find the sum of those multiplies.
    (3, 5, 20) => 98 (3 + 6 + 9 + 12 + 15 + 18 + 5 + 10 + 20) 15 is included only once
    (3, 3, 10) => 18 (3 + 6 + 9)
    (3, 10, 2) => 0
    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    summary = []
    first = first_num
    second = second_num
    while first <= limit:
        summary.append(first)
        first += first_num
    while second <= limit:
        summary.append(second)
        second += second_num
    return sum(list(set(summary)))


def count_odds_and_evens(numbers: list) -> str:
    r"""
    The task is to count how many odd and even numbers does the given list contain.

    Do not count zeros (0).
    Result should be displayed as string "ODDS: {number of odds}\nEVENS: {number of evens}"

    count_odds_and_events([1, 2, 3]) => "ODDS: 2\nEVENS: 1"
    count_odds_and_events([1, 0]) => "ODDS: 1\nEVENS: 0"

    :param numbers: list
    :return: str
    """
    odd = []
    even = []
    for i in numbers:
        if i == 0:
            continue
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f"ODDS: {len(odd)}\nEVENS: {len(even)}"


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5
    """
    num = 0
    two = 0
    five = 0
    status = False
    for i in numbers:
        if i == 2 and two <= five:
            two += 1
            status = True
        elif i == 5:
            five += 1
            status = False
        else:
            if status is True:
                num += i
            continue
    return num


def transcribe(dna_strand: str):
    """
    Write a function that returns a transcribed RNA strand from the given DNA strand.

    that is formed by replacing each nucleotide(character) with its complement: G => C, C => G, T => A, A => U
    Return None if it is not possible to transcribe a DNA strand.
    Empty string should return empty string.

    "ACGTGGTCTTAA" => "UGCACCAGAAUU"
    "gcu" => None

    :param dna_strand: original DNA strand
    :return: transcribed RNA strand in the uppercase or None
    """
    word = []
    dna = dna_strand.upper()
    if len(dna) == 0:
        return ""
    for i in dna:
        if i == "A":
            word.append("U")
        elif i == "T":
            word.append("A")
        elif i == "C":
            word.append("G")
        elif i == "G":
            word.append("C")
        else:
            return None
    return "".join(word)


def union_of_dict(d1: dict, d2: dict):
    """
    Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

    union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
    union_of_dict({}, {"bar": "foo"}) => {}
    """
    if len(d1) == 0 or len(d2) == 0:
        return {}
    k1 = []
    k2 = []
    dictionary = {}

    for i in d1:
        k1.append(i)
    for i in d1:
        k2.append(i)

    for i in k1:
        if i in d2:
            if d1[i] == d2[i]:
                dictionary[i] = d1[i]

    return dictionary


def reserve_list(input_strings: list) -> list:
    """Given list of strings, return new reversed list where each list element is reversed too."""
    status = True
    li = []
    for i in input_strings:
        if i == "python":
            li.append(i)
            status = False
        elif i == "java":
            li.append(i)
            status = True
        else:
            if status:
                li.append(i[::-1])
            else:
                li.append(i)
    return li[::-1]


def convert_binary_to_decimal(binary_list: list):
    """
    Extract binary codes of given length from list and convert to decimal numbers.

    [0, 0, 0, 0] => 0.
    [0, 1, 0, 0] => 4.

    :param binary_list: list of 1 and 0 (binary code)
    :return: number converted into decimal system
    """
    decimal = 0
    for i in range(0, len(binary_list)):
        decimal = decimal + int(binary_list[i]) * (2 ** (len(binary_list) - i - 1))
    return decimal


def print_pages(pages: str) -> list:
    """
    Find pages to print in console.

    examples:
    print_pages("2,4,9") -> [2, 4, 9]
    print_pages("2,4-7") -> [2, 4, 5, 6, 7]
    print_pages("2-5,7,10-12,17") -> [2, 3, 4, 5, 7, 10, 11, 12, 17]
    print_pages("1,1") -> [1]
    print_pages("") -> []
    print_pages("2,1") -> [1, 2]

    :param pages: string containing page numbers and page ranges to print.
    :return: list of pages to print with no duplicates, sorted in increasing order.
    """
    li = []
    for i in pages:
        if i.isdigit():
            li.append(i)
        elif i == "-":
            li.append(i)
        continue
    lis = []
    lit = []
    for i in range(len(li)):
        if li[i] == "-":
            lis.extend(help([li[i - 1], li[i + 1]]))
        lis.append(li[i])
    for i in lis:
        if i == "-":
            lis.remove(i)
    for i in lis:
        lit.append(int(i))
    return list(set(lit))


def help(lis):
    """Help."""
    li = []
    pervqi = int(lis[0])
    while pervqi < int(lis[1]):
        pervqi += 1
        li.append(pervqi)
    return li

