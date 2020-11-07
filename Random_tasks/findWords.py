def findWords(words):
    """
        :type words: List[str]
        :rtype: List[str]
        """
    first_row = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    second_row = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    third_row = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

    answer = []

    for word in words:
        this_word = word.lower()
        count_1 = 0
        count_2 = 0
        count_3 = 0
        print(this_word)
        for j in this_word:
            if j in first_row:
                count_1 += 1
            elif j in second_row:
                count_2 += 1
            elif j in third_row:
                count_3 += 1
        print(count_1, count_2, count_3)
        if count_1 == len(this_word):
            answer.append(word)
        elif count_2 == len(this_word):
            answer.append(word)
        elif count_3 == len(this_word):
            answer.append(word)

    return answer

words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))
