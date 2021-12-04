
# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
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
        validity = self.valid_words.copy()
        return validity

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
        default_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, 'A':26, 'B':27, 'C':28, 'D':29, 'E':30, 'F':31, 'G':32, 'H':33, 'I':34, 'J':35, 'K':36, 'L':37, 'M':38, 'N':39, 'O':40, 'P':41, 'Q':42, 'R':43, 'S':44, 'T':45, 'U':46, 'V':47, 'W':48, 'X':49, 'Y':50, 'Z':51,}
        shifted_dict = {item: (default_dict[item]+shift)%52 for item in default_dict}
        return shifted_dict
        
        
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
        revert_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z', 26:'A', 27:'B', 28:'C', 29:'D', 30:'E', 31:'F', 32:'G', 33:'H', 34:'I', 35:'J', 36:'K', 37:'L', 38:'M', 39:'N', 40:'O', 41:'P', 42:'Q', 43:'R', 44:'S', 45:'T', 46:'U', 47:'V', 48:'W', 49:'X', 50:'Y', 51:'Z',}
        shift_dict = self.build_shift_dict(shift)
        cyphyr = ""
        message_text = self.get_message_text()
        for letter in message_text:
            if letter.isalpha():
                cyphyr = cyphyr+revert_dict[shift_dict[letter]]
            else:
                cyphyr = cyphyr+letter
        return cyphyr
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        return


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words

    def build_decryption_dict(self, shift): #build a decryption dictionary
        #with the shift value passed in
        default_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z', 26:'A', 27:'B', 28:'C', 29:'D', 30:'E', 31:'F', 32:'G', 33:'H', 34:'I', 35:'J', 36:'K', 37:'L', 38:'M', 39:'N', 40:'O', 41:'P', 42:'Q', 43:'R', 44:'S', 45:'T', 46:'U', 47:'V', 48:'W', 49:'X', 50:'Y', 51:'Z',}
        shifted_dict = {(key+shift)%52: default_dict[key] for key in default_dict}
        return shifted_dict
    
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        def get_shift(shift, text):
            #returns shifted text and the number of matches, as a tuple.
            default_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52,}
            decryption_dict = self.build_decryption_dict(shift)
            dcyphyr = ""
            for letter in text:
                if letter.isalpha():
                    num = default_dict[letter]
                    shifted_letter = decryption_dict[num]
                    dcyphyr = dcyphyr+shifted_letter
                else:
                    dcyphyr = dcyphyr+letter
            valids_count=0
            for word in dcyphyr.split():
                if is_word(self.get_valid_words(), word.lower()):
                    valids_count+=1
            return (shift, valids_count, dcyphyr)

        text = self.get_message_text()
        shift_tuple=get_shift(0, text)
        for num in range(1,52):
            compare = get_shift(num, text)
            if compare[1]>shift_tuple[1]:
                shift_tuple=compare

        
        to_return = (shift_tuple[0], shift_tuple[2].lower())           
        return to_return
            

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())
    print("testcase 1: malted, shift 4")
    plaintext = PlaintextMessage('malted', 4)
    print("plaintext to cipher:")
    print('Expected Output :   qepxih')
    print('Actual Output : ', plaintext.get_message_text_encrypted())
    print("")
    
    cyphertext = CiphertextMessage('qepxih')
    print("cipher to plaintext")
    print('Expected Output :  malted')
    print('Actual Output : ', cyphertext.decrypt_message())
    print("")

    print("testcase 2: Zones, shift 12")
    print("plaintext to cipher: ")
    plaintext = PlaintextMessage('Zones', 12)
    print("Expected Output: lAzqE")
    print("Actual Output: ", plaintext.get_message_text_encrypted())
    print("")

    print("cipher to plaintext")
    cyphertext = CiphertextMessage('lAzqE')
    print("Expected Output : Zones")
    print("Actual Output :", cyphertext.decrypt_message())
    print("")
    
    #TODO: best shift value and unencrypted story 
    
    
    story = CiphertextMessage(get_story_string())
    print("")
    print(story.decrypt_message())
    
    """ 15, 'jack florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. he has been registered for classes at mit twice before, but has reportedly never passed aclass. it has been the tradition of the residents of east campus to become jack florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.'"""
