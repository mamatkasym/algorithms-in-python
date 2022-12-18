"""
Implementations of different custom compare functions for sorting
"""


def compare_int_strings(a: str, b: str) -> int:
    """
    :param a: string of digits, not leading 0
    :param b: string of digits, not leading 0
    :return: result of compare => [-1, 0, 1]
    """
    if len(a) > len(b):
        return 1
    elif len(b) > len(a):
        return -1
    else:
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(b[i]) > int(a[i]):
                return -1

        return 0
