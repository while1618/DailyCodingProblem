# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


def autocomplete(word_corpus, query):
    matched_words = []
    for i in range(0, len(word_corpus)):
        if query in word_corpus[i]:
            matched_words.append(word_corpus[i])
    return matched_words


print(autocomplete(['dog', 'deer', 'deal'], 'de'))
