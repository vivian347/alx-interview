#!/usr/bin/python3

"""validUTF8"""


def validUTF8(data):
    # Number of bytes in the current character
    num_bytes = 0

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xff

        if num_bytes == 0:
            # Determine the number of bytes in the current character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                # The byte doesn't start with 0, 110, 1110, or 11110
                return False
        else:
            # Check that the byte starts with 10
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

        # The data set is not a valid UTF-8 encoding if there are too many bytes for the character
        if num_bytes < 0:
            return False

    # The data set is not a valid UTF-8 encoding if there are still bytes needed to complete the last character
    return num_bytes == 0
