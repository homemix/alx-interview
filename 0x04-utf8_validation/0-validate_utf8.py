#!/usr/bin/python3
"""
returns True if the string is valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Validate UTF-8
    """
    for i in range(len(data)):
        if data[i] >> 7 == 0:
            continue
        elif data[i] >> 5 == 0b110:
            if i + 1 >= len(data) or data[i + 1] >> 6 != 0b10:
                return False
            i += 1
        elif data[i] >> 4 == 0b1110:
            if i + 2 >= len(data) or data[i + 1] >> 6 != 0b10 or \
                    data[i + 2] >> 6 != 0b10:
                return False
            i += 2
        elif data[i] >> 3 == 0b11110:
            if i + 3 >= len(data) or data[i + 1] >> 6 != 0b10 or \
                    data[i + 2] >> 6 != 0b10 or data[i + 3] >> 6 != 0b10:
                return False
            i += 3
        else:
            return False
    return True
