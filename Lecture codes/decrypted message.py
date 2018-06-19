import string


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    #>>> is_word(word_list, 'bat') return
    True
    #>>> is_word(word_list, 'asdf') return
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):

        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        self.lowercase_letters = string.ascii_lowercase  # day ki tu a-z
        self.uppercase_letters = string.ascii_uppercase  # day ki tu A_Z
        self.shift_dict = {}  # dictionary chua ky tu da ma hoa theo khoa shift (integer)
        for i in range(0, 26):  # i la chi so index cua day ky tu a-z, tu 0-25
            if (i + shift) > 25:
                remainder = (i + shift) % 26  # lay modulo 26
                self.shift_dict[self.lowercase_letters[i]] = self.lowercase_letters[remainder]
                self.shift_dict[self.uppercase_letters[i]] = self.uppercase_letters[remainder]
            else:
                self.shift_dict[self.lowercase_letters[i]] = self.lowercase_letters[i + shift]
                self.shift_dict[self.uppercase_letters[i]] = self.uppercase_letters[i + shift]
        return self.shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.build_shift_dict(shift)
        self.shifted_message_text = ""
        for letter in self.message_text:
            if letter in self.shift_dict:
                self.shifted_message_text += self.shift_dict[letter]
            else:
                self.shifted_message_text += letter
        return self.shifted_message_text


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        idea: giải mã_decrypt 1 chuỗi đã mã hóa với khóa shift không biết bằng cách:
        với mỗi khóa shift đi từ 0 đến 26 (26 chữ cái a-z):
        -so sánh mỗi từ của chuỗi đã mã hóa với danh sách word_list mà đề bài cho trước
        -nếu True thì ghi vết đếm số lượng từ khớp với danh sách
        -nếu khóa nào có số lượng từ khớp với danh sách word_list nhiều nhất thì in ra chuỗi với
        khóa shift đó
        -chuỗi mã hóa với khóa s thì chuỗi giải mã sẽ có khóa 26-s, thông tin để test
        '''
        global split_decrypted_msg, s, numer_words
        best_shift = 0
        max_number_words = 0

        for s in range(0, 26):  # 0<= x < 27
            decrypted_message = self.apply_shift(s)  # return string
            split_decrypted_msg = decrypted_message.split(' ')
            print(split_decrypted_msg )

            for word in split_decrypted_msg:  # so sanh vi word_list cho truoc
                numer_words = 0
                if is_word(self.valid_words, word):
                    numer_words += 1
                #print("number words: ", numer_words)
                if numer_words > max_number_words:
                    print("max number words: ", max_number_words)
                    max_number_words = numer_words
                    best_shift = s
                    print("best shift:", best_shift)
                #else:
                    #print("Cannot decrypt your encrypted message!!!\n because")

        return (26-best_shift, self.apply_shift(best_shift))

user_encrypted_msg = str(input("Enter string: "))
print("Message need to be decrypted: ", user_encrypted_msg)
ciphertext = CiphertextMessage(user_encrypted_msg)
#print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())