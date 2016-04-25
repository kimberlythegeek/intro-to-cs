# 6.00 Problem Set 3
# 
# Hangman
#

# purty stuff
import variables
import os.path
# Functions provided by the instructor
import helper_code
# MY FUNCTIONS #
import my_functions

# PROGRAM BEGINS #
num_guesses = 0
filename = ""

# While the user has not exited
while filename.lower() != "exit" and filename.lower() != "quit":

    filename = my_functions.select_file()

    # Break if user types quit or exit
    if filename.lower() == "exit" or filename.lower() == "quit":
        break

    # If no input, use default word list
    elif filename == "":
        filename = "words.txt"
        word_list = helper_code.load_words(filename)

    # Otherwise use custom word list
    else:

        # First check to see that the file exists
        while not os.path.isfile(filename):

            # If not, prompt again
            print variables.hr + "File not found! Please try again or hit Enter for the default word list:\n\n"
            filename = raw_input("\t>>>\t")
            # If no input, use default word list
            if filename == "":
                filename = "words.txt"

        word_list = helper_code.load_words(filename)

    # Continue running unless user inputs a negative value
    while num_guesses >= 0:

        # reset variables
        solved = False
        lost = False
        alphabet = []

        for character in variables.alphabet:
            alphabet.append(character)

        # Ask user how many guesses they want for the word
        print variables.hr + "\t\tCHOOSE DIFFICULTY\n\nHow many guesses would you like?\n"
        print "Hit Enter to use the default of 10\n\nType -1 to return to Main Menu\n\n"
        num_guesses = raw_input("\t>>>\t")

        # If no input, set number of guesses to default (10)
        if num_guesses == "":
            num_guesses = 10
        # If negative input, return to main menu
        elif int(num_guesses) < 0:
            break
        # Otherwise set it to user's choice
        else:
            num_guesses = int(num_guesses)

        # Initialize variables
        word = helper_code.choose_word(word_list)
        character_list = []
        found_list = []
        progress_list = []
        list_of_guesses = []

        # Tell user how long the word is
        print variables.hr + "\n\nNumber of letters in word: " + str(len(word))
        blanks = ""
        for character in word:
            blanks += " _ "

        print "\n" + blanks

        # Iterate through word
        for character in word:

            # Make a list from the word
            character_list.append(character)
            # Make a list to keep track of whether each letter has been found or not
            found_list.append(False)
            # Make a list to keep track of the partially guessed word to provide to the user
            progress_list.append("_")

        # While user has not guessed the word
        while not solved:

            if lost:
                break

            guess = ''

            # Print out the letters the user has NOT yet used
            print "\n\n\n" + (' '.join(alphabet)).upper() + "\n\n\n"

            # Ask user for their guess
            guess = raw_input("\tEnter a letter:")

            # Return to main menu if user types exit or quit
            if guess.lower() == "exit" or guess.lower() == "quit":
                break

            # Rather than restricting input to a single character, only take first character as guess
            else:
                guess = guess[0]

            # Check to see if user has already tried that letter
            # If so, tell them letter has been used. User will be prompted for another guess
            if my_functions.already_used_letter(guess, list_of_guesses, alphabet):
                print "\n\nYou have already used that letter!\n\n"

            # Otherwise, check to see if guess is in the word
            else:
                num_guesses = my_functions.check_guess(word, guess, num_guesses, character_list, found_list, progress_list)

            # Check to see if word has been solved
            solved = my_functions.word_guessed(word, found_list)
            if solved:
                print "\n\n Correct! The word was: " + word.upper()
                break

            # print "animation"
            my_functions.print_hangman(num_guesses)

            # If not solved, and out of guesses, end round
            if my_functions.lost_game(solved, num_guesses, word):
                break

            # Print partially guessed word
            print "\n\n\t" + (' '.join(progress_list)).upper()


