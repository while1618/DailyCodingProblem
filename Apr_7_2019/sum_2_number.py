# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def check_for_sum(list_of_numbers, k):
    for i in range(0, len(list_of_numbers) - 1):
        for j in range(i, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == k:
                return True
    return False


print(check_for_sum([10, 15, 3, 7], 17))
