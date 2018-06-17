key = 'abcdefgh'
plaintext = "igotosaigoN"
print(plaintext.islower())
print(key.index('e'))

print("Loading word list from file...")
# inFile: file
inFile = open("words.txt", 'r')
    # wordlist: list of strings
wordlist = []
for line in inFile:
    wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    print(wordlist)