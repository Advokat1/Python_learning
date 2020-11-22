def get_words(words):
    words_array = words.split()
    max_len = 0
    frequent_word = ''
    max_count = 0
    max_len_word = ''
    for word in words_array:
        print(word)
        f_count = 0
        for item in words_array:
            if item == word:
                f_count +=1

        if f_count > max_count:
            max_count = f_count
            frequent_word = word

        if len(word) > max_len:
            max_len = len(word)
            max_len_word = word        
    return frequent_word, max_len_word

print(get_words('test string old test lession'))