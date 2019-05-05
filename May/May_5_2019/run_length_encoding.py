# This problem was asked by Amazon.
#
# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def encode(string):
    encoded_string = ""
    counter = 1
    for i in range(0, len(string)):
        if i + 1 < len(string) and string[i] == string[i + 1]:
            counter += 1
        else:
            encoded_string += str(counter) + string[i]
            counter = 1
    return encoded_string


def decode(encoded_string):
    decoded_string = ""
    for i in range(0, len(encoded_string), 2):
        decoded_string += encoded_string[i + 1] * int(encoded_string[i])
    return decoded_string


print(encode("AAAABBBCCDAA"))
print(decode("4A3B2C1D2A"))
