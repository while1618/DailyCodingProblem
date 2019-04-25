# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


def lowest_possible_int_out_of_array(array_od_int):
    lowest_int = 1
    for i in range(0, len(array_od_int)):
        for j in range(i, len(array_od_int)):
            if abs(array_od_int[j]) == lowest_int:
                lowest_int += 1
                break

    return lowest_int


print(lowest_possible_int_out_of_array([1, 2, 0]))
