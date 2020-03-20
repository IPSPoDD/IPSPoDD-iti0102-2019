"""Encode and decode text using Rail-fence Cipher."""


def sik_sak(message: str, key: int):
    """Sik-sak liikumine.

    :param: message.
    :return: word
    """
    down_move = True
    row = 0
    result = ""
    for i in range(len(message[0])):
        result += message[row][i]
        if row == 0:
            row += 1
            down_move = True
        elif row == key - 1:
            row -= 1
            down_move = False
        elif down_move:
            row += 1
        elif not down_move:
            row -= 1
    return result


def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    replace_space = message.replace(" ", "_")

    if key == 1:
        return replace_space
    if key >= len(replace_space):
        return replace_space
    if key == 2:
        one = replace_space[0::2]
        two = replace_space[1::2]
        row_two = one + two
        return row_two
    if key == 3:
        one = replace_space[0::4]
        two = replace_space[1::2]
        three = replace_space[2::4]
        row_three = one + two + three
        return row_three

    result = ""
    matrix = [[""for x in range(len(replace_space))]for y in range(key)]
    increment = 1
    row = 0
    col = 0

    for c in replace_space:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[row][col] = c

        row += increment
        col += 1
    for list in matrix:
        result += "".join(list)

    return result


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    replace_line = message.replace("_", " ")

    if key == 1:
        return replace_line
    if key >= len(message):
        return replace_line

    result = ""

    matrix = [["" for x in range(len(replace_line))] for y in range(key)]

    idx = 0
    increment = 1

    for selectedRow in range(0, len(matrix)):
        row = 0
        for col in range(0, len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += replace_line[idx]
                idx += 1
            row += increment
    matrix = transpose(matrix)
    for list in matrix:
        result += "".join(list)

    return result


def transpose(m):
    """
    Reverse the table.

    :param m:
    :return:
    """
    result = [[0 for y in range(len(m))]for x in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result


if __name__ == '__main__':
    print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    print(encode("Mind on", 3))  # => M_idonn
    print(encode("hello", 1))  # => hello
    print(encode("hello", 8))  # => hello
    print(encode("kaks pead", 1))  # => kaks_pead

    print(decode("kaks_pead", 1))  # => kaks pead
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida
