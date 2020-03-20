"""The regular expressions."""
import re


def read_file(path: str) -> list:
    """
    Read file and return list of lines read.

    :param path: str
    :return: list
    """
    with open(path, encoding='utf-8') as text_file:
        return text_file.read().splitlines()


def match_specific_string(input_data: list, keyword: str) -> int:
    """
    Check if given list of strings contains keyword.

    Return all keyword occurrences (case insensitive). If an element cointains the keyword several times, count all the occurrences.

    ["Python", "python", "PYTHON", "java"], "python" -> 3

    :param input_data: list
    :param keyword: str
    :return: int
    """
    if len(keyword) == 0:
        return 0
    data = "".join(input_data)
    regex = "" + keyword + ""
    count = len(re.findall(regex, data, re.IGNORECASE))
    return count


def detect_email_addresses(input_data: list) -> list:
    """
    Check if given list of strings contains valid email addresses.

    Return all unique valid email addresses in alphabetical order presented in the list.
    ["Test", "Add me test@test.ee", "ago.luberg@taltech.ee", "What?", "aaaaaa@.com", ";_:Ö<//test@test.au??>>>;;d,"] ->
    ["ago.luberg@taltech.ee", "test@test.au", "test@test.ee"]

    :param input_data: list
    :return: list
    """
    f = []
    for d in input_data:
        obj = re.search(r"[0-9a-zA-Z.+_-]+@[0-9a-zA-Z]+.[a-zA-Z'._+-]+", d)
        if obj:
            c = obj.group()
            f.append(c)
    return sorted(set(f))


if __name__ == '__main__':

    list_of_lines_emails = read_file("input_detect_email_addresses_example_1.txt")  # reading from file
    print(detect_email_addresses(list_of_lines_emails))  # ['allowed@example.com', 'firstname-lastname@example.com', 'right@example.com', 'spoon@lol.co.jp', 'testtest@dome.museum', 'testtest@example.name']

    list_of_lines_keywords = read_file("input_match_specific_string_example_1.txt")
    print(match_specific_string(list_of_lines_keywords, "job"))  # 9
