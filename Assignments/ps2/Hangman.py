# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return sorted(list(secret_word)) == sorted(letters_guessed) or secret_word in get_guessed_word(secret_word, letters_guessed)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_list = list(secret_word)
    guessed_word_list = secret_word_list[:]
    for index, char in enumerate(secret_word_list):
      if char not in letters_guessed:
        guessed_word_list[index] = '_ '
    guessed_word = ''.join(guessed_word_list)
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ''
    return ''.join(sorted(set(list(all_letters))- set(letters_guessed)))
  
def is_letter_in_word(secret_word, letter):
  return letter in secret_word
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses
      
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game hangman!')
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("I'm thinking of a word that is", len(secret_word), 'letters long.')
    print("You have 3 warnings.")
    print('---------------------')
    
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
      print('You have', guesses, 'guesses left.\nAvailable letters:', get_available_letters(letters_guessed))
      letter = input('Please guess a letter:').lower()
      #check if it's a letter or a word
      if len(letter) <= 1:
        #check if letter is valid
        if letter in string.ascii_lowercase and letter != '':
          #has letter been guessed?
          if letter not in letters_guessed:
            letters_guessed.append(letter)
            #is letter in secret word?
            if letter in secret_word:
              print('Good guess:', end = ' ')
            else:
                list = ["a","o","i","u","e"]
                if letter  not in list:
                    guesses -= 1
                else:
                    guesses -= 2
                print("Opps! That letter is not in my word:", end = ' ')
          else:
          #subtract warning for guessing the samething again
            warnings -=1
            print("Oops! You've already guessed that letter.")
            print("You have", warnings, 'warnings left:', end = ' ')
        else:
        #subtract a warning for a non-letter/word
          warnings -=1
          print("Opps! That is not a valid letter.")
          print("You have", warnings, 'warnings left:', end = ' ')
      else:
      #check if it's the correct word
        if is_word_guessed(secret_word, list(letter)) and len(letter) == len(secret_word):
          letters_guessed = list(letter)
          print('You got it!')
        else:
          #subtract guess for incorrect guess
          guesses -= 1
          print("Opps! That is not the word I'm thinking of:", end = ' ')
      print(get_guessed_word(secret_word, letters_guessed))
      print('---------------------')
    
    #winner message
    if is_word_guessed(secret_word, letters_guessed):
      print('Congratulations, you won!\nYour total score for this game is', len(set(secret_word)) * guesses)
    #loser message
    else:
      print('Sorry, you ran out of guesses. The word was', secret_word)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    count = 0
    match = False
    my_word_wo_spaces = ''.join(my_word.split())
    if len(my_word_wo_spaces) == len(other_word):
      for index, char in enumerate(my_word_wo_spaces):
        if char == other_word[index] or char == '_':
          count += 1
          if count == len(other_word):
            match = True
            break
    return match
            
      


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ''
    for word in wordlist:
      if match_with_gaps(my_word, word):
        possible_matches += word + " "
    if len(possible_matches) == 0:
      return 'No possible matches found.'
    else:
      return possible_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game Hangman With Hints!')
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("I'm thinking of a word that is", len(secret_word), 'letters long.')
    print("You have 3 warnings.")
    print('---------------------')
    
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
      print('You have', guesses, 'guesses left.\nAvailable letters:', get_available_letters(letters_guessed))
      letter = input('Please guess a letter or guess the whole word:').lower()
      #check if it's a letter or a word
      if len(letter) <= 1:
        #check if they entered * for a hint
        if letter == '*':
          print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        else:
          #check if letter is valid
          if letter in string.ascii_lowercase and letter != '':
            #has letter been guessed?
            if letter not in letters_guessed:
              letters_guessed.append(letter)
              #is letter in secret word?
              if letter in secret_word:
                print('Good guess:', end = ' ')
              else:
                  list = ["a","o","i","u","e"]
                  if letter not in list:
                      guesses -=1
                  else:
                      guesses -= 2
                  print("Opps! That letter is not in my word:", end = ' ')
            else:
            #subtract warning for guessing the samething again
              warnings -=1
              print("Oops! You've already guessed that letter. You have", warnings, 'warnings left:', end = ' ')
          else:
          #subtract a warning for a non-letter/word
            warnings -=1
            print("Opps! That is not a valid letter. You have", warnings, 'warnings left:', end = ' ')
      else:
      #check if it's the correct word
        if is_word_guessed(secret_word, list(letter)) and len(letter) == len(secret_word):
          letters_guessed = list(letter)
          print('You got it!')
          break
        else:
          #subtract guess for incorrect guess
          guesses -= 1
          print("Opps! That is not the word I'm thinking of:", end = ' ')
      print(get_guessed_word(secret_word, letters_guessed))
      print('---------------------')
    
    #winner message
    if is_word_guessed(secret_word, letters_guessed):
      print('Congratulations, you won!\nYour total score for this game is', len(set(secret_word)) * guesses)
    #loser message
    else:
      print('Sorry, you ran out of guesses. The word was', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
   # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
   #hangman(secret_word)
    hangman(secret_word)


