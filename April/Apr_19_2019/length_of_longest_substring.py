# This problem was asked by Amazon.
#
# Given an integer k and a string s,
# find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring(k, s):
    results = []
    for i in range(0, len(s) - 1):
        temp = ''
        for j in range(i, len(s)):
            if len(temp) >= k and s[j] not in temp:
                break
            temp += s[j]
        results.append(temp)
    return max(results, key=len)


print(longest_substring(2, 'abcba'))
