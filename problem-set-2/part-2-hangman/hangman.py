# 6.00 Problem Set 3
# 
# Hangman
#



# purty stuff
import pt2_variables

import os.path

# Functions provided by the instructor

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string


def load_words(filename):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print pt2
    pt2_variables.hr + "\t\tLoading word list from file..."
    # inFile: file
    inFile = open(filename, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print " \n\t\t", len(wordlist), "words loaded from " + filename
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------






# MY FUNCTIONS #

# Check to see if all letters in the word have been guessed
def word_guessed():
    i = 0
    # Check to see if word has been guessed
    for char in word:
        if not found_list[i]:
            # print "\nword unsolved\n"
            return
        i += 1
    print '\nword solved!\n'
    solved = True
    return solved



# Check to see if the user has already used this letter
# Will not deduct guesses for a wrong letter entered more than once
def already_used_letter(guess):
    for char in list_of_guesses:
        if guess == char:
            return True

    # If not already used, remove letter from alphabet list to show user what letters are left
    list_of_guesses.append(guess)
    remove_letter(guess)
    return False


# Remove letter from alphabet list to show user what letters are left
def remove_letter(guess):
    i = 0
    for character in alphabet:
        if guess == character:
            alphabet[i] = " "
            return
        i += 1



# Check to see if letter is in the word
def check_guess(num_guesses):
    guess_flag = False
    i = 0
    print pt2_variables.hr

    # Check to see if the user's guess is in the word
    for char in word:
        if guess.lower() == character_list[i]:
            found_list[i] = True
            progress_list[i] = character_list[i]
            guess_flag = True
            print "\n\n\t\tCharacter found! Good guess!\n\n"

        i += 1

    # Check to see if the guess was found. If not, deduct one guess
    if not guess_flag:
        num_guesses -= 1
        print "\n\n\t\tCharacter not found :( Lost one guess"

    # Tell User how many guesses are left
    print "\n\n\t\tGUESSES REMAINING: " + str(num_guesses) + "\n\n\n"
    return num_guesses






# PROGRAM BEGINS #
num_guesses = 0
filename = ""

# While the user has not exited
while filename.lower() != "exit" and filename.lower() != "quit":

    print pt2_variables.hangman

    # Get file name for word list from user
    print pt2_variables.hr + "Enter the full file name of the word list you would like to use\n"
    print "Hit Enter to use the default wordlist, words.txt\n\nType quit to exit the program\n\n"
    filename = raw_input("\t>>>\t")

    # Break if user types quit or exit
    if filename.lower() == "exit" or filename.lower() == "quit":
        break

    # If no input, use default word list
    elif filename == "":
        filename = "words.txt"
        wordlist = load_words(filename)


    # Otherwise use custom word list
    else:

        # First check to see that the file exists
        while not os.path.isfile(filename):

            # If not, prompt again
            print pt2_variables.hr + "File not found! Please try again or hit Enter for the default word list:\n\n"
            filename = raw_input("\t>>>\t")
            # If no input, use default word list
            if filename == "":
                filename = "words.txt"

        wordlist = load_words(filename)

    # Continue running unless user inputs a negative value
    while num_guesses >= 0:

        # reset variables
        solved = False
        lost = False
        alphabet = []

        for character in pt2_variables.alphabet:
            alphabet.append(character)

        # Ask user how many guesses they want for the word
        print pt2_variables.hr + "\t\tCHOOSE DIFFICULTY\n\nHow many guesses would you like?\n"
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
        word = choose_word(wordlist)
        character_list = []
        found_list = []
        progress_list = []
        list_of_guesses = []


        # print word


        # Tell user how long the word is
        print pt2_variables.hr + "\n\nNumber of letters in word: " + str(len(word))
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
            if already_used_letter(guess):
                print "\n\nYou have already used that letter!\n\n"

            # Otherwise, check to see if guess is in the word
            else:
                num_guesses = check_guess(num_guesses)

            # Check to see if word has been solved
            solved = word_guessed()
            if solved:
                print "\n\n Correct! The word was: " + word.upper()
                break

            if num_guesses > 5:
                print pt2_variables.hangman_picture_6
            elif num_guesses == 5:
                print pt2_variables.hangman_picture_5
            elif num_guesses == 4:
                print pt2_variables.hangman_picture_4
            elif num_guesses == 3:
                print pt2_variables.hangman_picture_3
            elif num_guesses == 2:
                print pt2_variables.hangman_picture_2
            elif num_guesses == 1:
                print pt2_variables.hangman_picture_1

            # If not solved, and out of guesses, end round
            if not solved and num_guesses == 0:
                print pt2_variables.hr + pt2_variables.hangman_picture_0 + "\n\n you lost :( out of guesses\n\n"
                print "\n\n\tThe word was: " + word.upper()
                lost = True
                break

            # Print partially guessed word
            print "\n\n\t" + (' '.join(progress_list)).upper()


