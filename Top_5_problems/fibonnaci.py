# Write a function that computes the list of the first 100 Fibonacci numbers.
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
# and each subsequent number is the sum of the previous two.
# As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.


def fibonnaci(number):
    result = [0, 1]
    for i in range(2, number):
        result.append(result[i - 1] + result[i - 2])
    return result


print(fibonnaci(100))
