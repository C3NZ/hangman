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
    
    correct_letters_needed = len(secret_word)
    correct_letters = 0

    #Iterate through all the letters the user has guessed 
    #and count the amount of times each letters appears 
    #in the secret word. You can determine that the word is
    #guessed when the sum of the appearances of characters guessed by the user
    #in the secret_word string is equal to the length of the secret word
    for letter in letters_guessed:        
        correct_letters += secret_word.count(letter)
            
        if correct_letters == correct_letters_needed:
            return True

    return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    guessed_word = [' _ ' for i in range(len(secret_word))]
    
    #Go over each character in the secret word and update
    #what the user has guessed so far
    if len(letters_guessed)  == 0:
        return "".join(guessed_word)
    else:
        for i in range(len(secret_word)):
            if secret_word[i] in letters_guessed:
                guessed_word[i] = secret_word[i]

        return "".join(guessed_word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    available_letters = [char for char in string.ascii_lowercase]
    
    #If the user hasn't guessed anything yet, all chars are available
    if len(letters_guessed) == 0:
        return "".join(available_letters)
    else:
        for letter in letters_guessed:
            if letter in available_letters:
                available_letters.remove(letter)

    return "".join(available_letters)
    

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
    
    #Initialize all important variables
    num_guesses = 6
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    game_is_won = False
    warnings = 3

    #Greet the user
    print("\nWelcome to Hangman!\nthe secret letter has",
          len(secret_word), "letters in it.")
    print("----------------\n")

    while num_guesses > 0 and not game_is_won:
        
        print("You have", num_guesses, "of guesses left")
        print("Here are your available characters: " + available_letters)
        print("This is the word so far:", get_guessed_word(secret_word, letters_guessed))
        
        guess = str(input("Enter your next guess:")).lower()
        
       #Force the user to provide correct input if they didn't already
        while guess not in available_letters or len(guess) != 1:      
            
            #Punish the user for not entering 
            if guess not in string.ascii_lowercase:
                print("\nYou entered something other than a letter!")
                
                if warnings == 0:
                    num_guesses -= 1
                    print("You have", num_guesses, "of guesses left\n")
                else:
                    warnings -= 1
                    print("you have", warnings, "warnings left")
                
                if num_guesses == 0:
                    break   
                    
            else:
                print("\nThat guess is either too long or has been used already!\n")

            #Get the users input and try again
            guess = str(input("Enter your next guess:")).lower()
       

        #Add the guessed letter to the list and then remove it
        #from available characters
        letters_guessed.append(guess)
        available_letters = get_available_letters(letters_guessed)

        #Act on whether the user guessed the word correctly or not
        if guess in secret_word:
            
            print("\nCongrats, you've guessed a correct character!\n")
            
            #check if the word has been fully guessed
            if is_word_guessed(secret_word, letters_guessed):
                print("Congratulations, you won! The word was: " + secret_word + '\n')
                print("Your score is:", (num_guesses * len([char for char in letters_guessed if char in secret_word])))
                game_is_won = True              
        
        else:
           
            print("\nThat letter is not in the secret word!\n")
            
            if guess in 'aeiou':
                num_guesses -= 2
            else:
                num_guesses -= 1

            if num_guesses <= 0:
                print("You have run out of guesses and have lost!")
                print("The correct word was: " + secret_word + '\n')
        
        print("-----------")
        
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

    my_word = my_word.replace(' ', '')
    
    #if the length of the words do not match then neither can the words
    if len(my_word) != len(other_word):
        return False

    #compare the word we've guessed so far to another word
    for i in range(len(my_word)):
        if my_word[i] != other_word[i] and (my_word[i] != '_' or other_word[i] in my_word):
            return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    #List that will contain all possible matches
    possible_matches = []
    
    #Iterate through every word in our word list and run it through
    #our match_with_gaps functions to find potential matches
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    #Print out the result after evaulating all words in the wordlist
    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print("\nHere are some Possible matches:\n" + " ".join(possible_matches) + '\n')



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
    
    #hangman game vars
    num_guesses = 6
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    game_is_won = False
    warnings = 3

    #Greet the user
    print("\nWelcome to Hangman!")
    print("I'm thinking of a word that has", len(secret_word), "letters in it")
    print("----------------\n")

    #Start the game
    while num_guesses > 0 and not game_is_won:
        
        #Provide the user with information about their current game session
        print("You have", num_guesses, "of guesses left")
        print("Available characters: " + available_letters)
        print("This is the word so far:", get_guessed_word(secret_word, letters_guessed))
        
        guess = input("Enter your next guess:").lower()
        
        #only enter loop if the user didn't provide the correct input
        while (guess not in available_letters and guess != '*') or len(guess) != 1 :      
            
            #Determine the output to show based on 
            if guess not in string.ascii_lowercase:
                print("\nYou entered something other than a letter!")
            elif len(guess) > 1:
                print("\nYou entered more than one character as a guess!")
            else:
                print("\nThat character has been used already!\n")

            #Penalize the user for breaking the rules of the game
            if warnings == 0:
                num_guesses -= 1
                print("You have", num_guesses, "of guesses left\n")
            else:
                warnings -= 1
                print("you have", warnings, "warnings left")
                
            if num_guesses == 0:
                break  

            guess = str(input("Enter your next guess:")).lower()
        
       
        #checks whether or not if the user used the hint key or made an actual guess
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue    
        else:
            letters_guessed.append(guess)
            available_letters = get_available_letters(letters_guessed)
        
        
        #Act on whether the user has guessed a correct letter or not
        if guess in secret_word:
            
            print("\nCongrats, you've guessed a correct character!\n")
            
            #Check to see if all letters have been guessed
            if is_word_guessed(secret_word, letters_guessed):

                print("Congratulations, you won! The word was: " + secret_word + '\n')
                print("Your total score for this game is:", (num_guesses * len([char for char in letters_guessed if char in secret_word])))
                game_is_won = True

        else:
            
            print("\nThat letter is not in the secret word!\n")
            
            #Determine how many guesses the user loses for an incorrect guess
            if guess in 'aeiou':
                num_guesses -= 2
            else:
                num_guesses -= 1

            #The user has ran out of guesses
            if num_guesses <= 0:
                
                print("Sorry, you have run out of guesses and have lost the game.")
                print("The correct word was: " + secret_word + '\n')
        
        print("-----------")


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
