# This problem was asked by Facebook.
#
# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.


import random


def pick_random(stream_of_elements):
    return stream_of_elements[int(random.uniform(0, len(stream_of_elements)))]


print(pick_random(['a', 'b', 'c', 'd', 'e', 'f']))
