# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

#import string
#from ps4a import get_permutations
from ps4b import Message

### HELPER CODE ###
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
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(Message):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        #pass #delete this line and replace with your code here
    
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
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        lower_letters_to_values = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4,
            'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15, 'p': 16,
            'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26}

        lower_values_to_letters = {
            1: 'a', 2: 'b', 3: 'c', 4: 'd',
            5: 'e', 6: 'f', 7: 'g', 8: 'h',
            9: 'i', 10: 'j', 11: 'k', 12: 'l',
            13: 'm', 14: 'n', 15: 'o', 16: 'p',
            17: 'q', 18: 'r', 19: 's', 20: 't',
            21: 'u', 22: 'v', 23: 'w', 24: 'x',
            25: 'y', 26: 'z' }

        upper_letters_to_values = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4,
            'E': 5, 'F': 6, 'G': 7, 'H': 8,
            'I': 9, 'J': 10, 'K': 11, 'L': 12,
            'M': 13, 'N': 14, 'O': 15, 'P': 16,
            'Q': 17, 'R': 18, 'S': 19, 'T': 20,
            'U': 21, 'V': 22, 'W': 23, 'X': 24,
            'Y': 25, 'Z': 26 }

        upper_values_to_letters = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D',
            5: 'E', 6: 'F', 7: 'G', 8: 'H',
            9: 'I', 10: 'J', 11: 'K', 12: 'L',
            13: 'M', 14: 'N', 15: 'O', 16: 'P',
            17: 'Q', 18: 'R', 19: 'S', 20: 'T',
            21: 'U', 22: 'V', 23: 'W', 24: 'X',
            25: 'Y', 26: 'Z'  }
        def transpose_dict(dictionary, vowels_permutation):
            dict = {}
            # The key should be a letter and the value should be a number
            for key in dictionary:
                # checking that when i add the shift to the value the value doesn't exceed the size of the alphabet.
                if dictionary[key] ==1:
                    dict[key] = (dictionary[key] + 4)
                # if it does exceed the size i subtract the size of the alphabet to start counting from beginning
                elif dictionary[key] ==5:
                    dict[key] = (dictionary[key] -4)
                
                elif dictionary[key] ==9:
                    dict[key] = dictionary[key]
                elif dictionary[key] ==15:
                    dict[key] = (dictionary[key] + 6)
                # if it does exceed the size i subtract the size of the alphabet to start counting from beginning
                elif dictionary[key] ==21:
                    dict[key] = (dictionary[key] - 6)
            return dict

        # function switches the keys and values of a dictionary
        def inv_dict(dictionary):
            dictmap = {}
            for key in dictionary:
                dictmap[dictionary[key]] = key
            return dictmap

        # since the keys should now be number's mapped to a new letter, i replace the number with its original letter
        def change_keys_to_letters(dictionary, mapping):
            dict = {}
            for key in dictionary:
                dict[mapping[key]] = dictionary[key]
            return dict

        def put_it_all_together(dictionary, vowels_permutation, reference_table):
            local_dictionary = transpose_dict(dictionary, vowels_permutation)
            local_dictionary = inv_dict(local_dictionary)
            local_dictionary = change_keys_to_letters(local_dictionary, reference_table)
            local_dictionary = inv_dict(local_dictionary)

            return local_dictionary

        shifted_lower = put_it_all_together(lower_letters_to_values, vowels_permutation, lower_values_to_letters)
        shifted_upper = put_it_all_together(upper_letters_to_values, vowels_permutation, upper_values_to_letters)

        return {**shifted_lower, **shifted_upper}
       
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        dictionary = self.build_transpose_dict(transpose_dict)
        text = self.get_message_text()
        transpose_text = ''
        for char in text:
            try:
                transpose_text = transpose_text + dictionary[char]
            except KeyError:
                transpose_text = transpose_text + char
        return transpose_text
      
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        final_shift = 0
        best_word_list = 0
        word_list = load_words('words.txt')
        for shift in range(1,27):
            decrypted_text = self.apply_transpose(shift)
            wordlist = decrypted_text.split(' ')
            num_valid_words = 0
            for word in wordlist:
                if is_word(word_list, word):
                    num_valid_words += 1
            if num_valid_words > best_word_list:
                final_shift = shift
                best_word_list = num_valid_words

        return (final_shift, self.apply_transpose(final_shift))
    

if __name__ == '__main__':

    #print(get_permutations('eaiuo'))
    # Example test case
    message = SubMessage("Hello World!")
    
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print(enc_dict)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    str=input('Enter a string:')
    message=SubMessage(str)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
