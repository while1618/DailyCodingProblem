# This problem was asked by Facebook.
#
# Implement regular expression matching with the following special characters:
#
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not
# the string matches the regular expression.
#
# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.
#
# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.


def regular_expression(string, regex):
    if (len(string) > len(regex) and regex[-1] != '*') or len(string) < len(regex):
        return False
    string_index = 0
    for i in range(0, len(regex)):
        if regex[i] == string[string_index]:
            string_index += 1
        elif regex[i] == '.':
            string_index += 1
        elif regex[i] == '*':
            if i + 1 < len(regex):
                for j in range(string_index, len(string)):
                    if string[j] == regex[i + 1]:
                        string_index = j
                        break
        else:
            return False
    return True


print(regular_expression('ray', 'r*'))
print(regular_expression('raymond', 'ra.'))
print(regular_expression('chat', '.*at'))
print(regular_expression('chats', '.*at'))
