# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be:
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


def product_of_all_numbers(array_of_integers):
    new_array = []
    for i in range(0, len(array_of_integers)):
        product = 1
        for j in range(0, len(array_of_integers)):
            if i != j:
                product *= array_of_integers[j]
        new_array.append(product)
    return new_array


print(product_of_all_numbers([1, 2, 3, 4, 5]))
