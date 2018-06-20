SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
word = 'abcd'
first = 0
for letter in word:
    first += SCRABBLE_LETTER_VALUES.get(letter)
print(first+2)

word = word.lower()
first_component = 0
for letter in word:
        first_component += SCRABBLE_LETTER_VALUES.get(letter)
print(first_component +5)

words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308}
key_list = list(words.keys())
print(key_list)
print(key_list[0])
for (word, n) in words.keys():
    word = word.lower()
    print(word,n)
    for letter in word:
        first_component += SCRABBLE_LETTER_VALUES.get(letter)
print(first_component)