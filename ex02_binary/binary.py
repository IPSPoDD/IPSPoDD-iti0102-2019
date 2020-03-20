"""Converter."""


def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    if dec == 0:
        return str(0)
    elif dec < 0:
        return False
    else:
        binary = ""
        while dec > 0:
            binary = str(dec % 2) + binary
            dec = dec // 2
        return binary


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    length = len(binary)
    decimal = 0
    for i in range(0, length):
        decimal = decimal + int(binary[i]) * (2 ** (length - i - 1))
    return decimal
