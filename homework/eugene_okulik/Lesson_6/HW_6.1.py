text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
new_text = []
for word in words:
    if word[-1] in {',', '.'}:
        spec_character = word[-1]
        base = word[:-1]
        new_word = base + 'ing' + spec_character
    else:
        new_word = word + 'ing'
    new_text.append(new_word)
print(' '.join(new_text))
