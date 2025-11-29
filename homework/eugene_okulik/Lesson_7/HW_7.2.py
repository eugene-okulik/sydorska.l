def my_words(words):
    for keys, values in words.items():
        print(keys * values)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
my_words(words)
