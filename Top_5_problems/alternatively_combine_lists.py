# Write a function that combines two lists by alternatingly taking elements.
# For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].


def alternatively_combine(list1, list2):
    result = []
    bigger_list_len = len(list1) > len(list2) and len(list1) or len(list2)
    for i in range(0, bigger_list_len):
        if len(list1) > i:
            result.append(list1[i])
        if len(list2) > i:
            result.append(list2[i])
    return result


print(alternatively_combine(['a', 'b', 'c', 'd'], [1, 2, 3]))
