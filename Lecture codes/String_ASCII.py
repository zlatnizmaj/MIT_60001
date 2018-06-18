import string
str = "12345 string strip function in Python 00000 ttlllggg"
str_striped = str.strip("1,g") # remove all matched character begin and end of string
print(str_striped)

letter_list = string.ascii_lowercase + string.ascii_uppercase
print(letter_list)
print(ord('A'))
letter_dict = {}
print(str.index('1'))
str2 ="12345"
print(''.join(reversed(str2)))

word="guru99 career guru99"
print(word.split('r')) # split the string wherever 'r' is mentioned in the string
print(word.split('99'))

x = "Guru99"
x.replace("Guru99","Python")
x = x.replace("Guru99","Python")
print(x) # will still return Guru99. This is because x.replace("Guru99","Python") returns a copy of X with replacements made


lowercase_letter = string.ascii_lowercase
print(lowercase_letter)
shift = 1
shift_dict = {}
for i in range(0, 26):  # i la chi so index cua day ky tu a-z, tu 0-25
    if (i + shift) > 25:
        remainder = (i + shift) % 26  # lay modulo 26
        shift_dict[lowercase_letter[i]] = lowercase_letter[remainder]
        print("{} - {}".format(lowercase_letter[i], lowercase_letter[remainder]))

    else:
        print("{} - {}".format(lowercase_letter[i], lowercase_letter[i + shift]) )
        shift_dict[lowercase_letter[i]] = lowercase_letter[i + shift]
print(shift_dict)

message_text = "i love you"
print(message_text.strip())
cipher_message_text = ""
for letter in message_text:
    if letter in shift_dict:
        cipher_message_text += shift_dict[letter]
    else:
        cipher_message_text += letter # giu nguyen ky tu khoanrg trang vaf dac biet khong phai a-z
print(cipher_message_text)
