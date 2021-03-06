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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
    	if letter not in letters_guessed:
    		return False
    return True
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = ""
    for letter in secret_word:
    	if letter in letters_guessed:
    		guessed = guessed+letter
    	else:
    		guessed = guessed+"_ "
    return guessed



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    avail = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
    	if not char in letters_guessed:
    		avail = avail+char
    return avail

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 0
    letters_guessed = []
    print("Welcome to hangman. ")
    print("I'm thinking of a word which is " + str(len(secret_word)) + " ")
    print("letters long.")
    while (guesses > 0) and not is_word_guessed(secret_word, letters_guessed):
        print("")
        print("Secret word: " + get_guessed_word(secret_word, letters_guessed))
        print("Available Letters: " + str(get_available_letters(letters_guessed)))

        warned = warnings
        guessed = guesses
        #make sure that we don't decrement guesses on turns
        #which result in a warning
        guess = input("Please guess a letter: ")
        if not guess.isalpha():
            if warnings < 3:
                warnings+=1
            else:
                guesses-=1
            print("")
            print("Please enter a letter. Number of warnings: " +  str(warnings))
            print("")
            print("___________________")

        if guess in letters_guessed:
            if warnings < 3:
                warnings+=1
            else: guesses-=1
            print("")
            print("You have already guessed that letter. Please enter a new one.")
            print("Number of warnings: " + str(warnings))
            print("")
            print("___________________")

        if type(guess)==str and len(guess) != 1:
            warnings+=1
            print("")
            print("Please enter a single letter. Number of warnings: "+ str(warnings))
        
        if warnings == warned and guesses == guessed: #execute if no new warnings this iteration, and no guesses expended on redundant guess
            guess = guess.lower()
            letters_guessed.append(guess)
            if guess not in secret_word:
                print("Incorrect guess. ")
                print("")
    
                if guess in 'aeiou':
                    guesses-=2
                else:
                    guesses-=1
            else:
                print("Correct guess. ")
                print("Word: " + get_guessed_word(secret_word, letters_guessed))
                print("")
 
        print("You have " + str(max(guesses,0)) + " guesses remaining.")
        print("")
        print("___________________")

       
    if guesses <= 0:
        print("Game Over: No more guesses.")
        print("Secret word: " + secret_word)
    if is_word_guessed(secret_word, letters_guessed):
        print("You Win!")
        print("Secret word: " + secret_word)
    
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
    #assume my_word has been modified to be the same length as the words it matches with

    if len(my_word) == len(other_word):
        k=0
        for letter in my_word:
            if letter == "_":
                if other_word[k] in my_word:
                    return False
            else:
                if other_word[k] != letter:
                    return False
            k+=1
        return True
    return False

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
    my_word = my_word.replace(" ", "")
    print("")
    print("Possible Matches: ")
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word + " ", end=' ')
    print("")
    
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
    
    
    guesses = 6
    warnings = 0
    letters_guessed = []
    print("Welcome to hangman. ")
    print("I'm thinking of a word which is " + str(len(secret_word)) + " ")
    print("letters long.")
    while (guesses > 0) and not is_word_guessed(secret_word, letters_guessed):
        print("")
        print("Secret word: " + get_guessed_word(secret_word, letters_guessed))
        print("Available Letters: " + str(get_available_letters(letters_guessed)))

        warned = warnings
        guessed = guesses
        #make sure that we don't decrement guesses on turns
        #which result in a warning
        guess = input("Please guess a letter: ")
        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        if not guess.isalpha() and not guess == "*":
            if warnings < 3:
                warnings+=1
            else:
                guesses-=1
            print("")
            print("Please enter a letter. Number of warnings: " +  str(warnings))
            print("")
            print("___________________")

        if guess in letters_guessed:
            if warnings < 3:
                warnings+=1
            else: guesses-=1
            print("")
            print("You have already guessed that letter. Please enter a new one.")
            print("Number of warnings: " + str(warnings))
            print("")
            print("___________________")

        if type(guess)==str and len(guess) != 1:
            warnings+=1
            print("")
            print("Please enter a single letter. Number of warnings: "+ str(warnings))
        
        if warnings == warned and guesses == guessed and guess != "*": #execute if no new warnings this iteration, and no guesses expended on redundant guess
            guess = guess.lower()
            letters_guessed.append(guess)
            if guess not in secret_word:
                print("Incorrect guess. ")
                print("")
    
                if guess in 'aeiou':
                    guesses-=2
                else:
                    guesses-=1
            else:
                print("Correct guess. ")
                print("Word: " + get_guessed_word(secret_word, letters_guessed))
                print("")
 
        print("You have " + str(max(guesses,0)) + " guesses remaining.")
        print("")
        print("___________________")

       
    if guesses <= 0:
        print("Game Over: No more guesses.")
        print("Secret word: " + secret_word)
    if is_word_guessed(secret_word, letters_guessed):
        print("You Win!")
        print("Secret word: " + secret_word)
        


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
