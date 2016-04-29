import os.path
import helper_functions
import variables

# ----------------------------------------------------
# Opening screen and file selection

def select_file():
    filename = ""

    # Get file name for word list from user
    print "\n\n\n" + "-" * 100 + "\n\n\n"
    print "Enter the full file name of the word list you would like to use\n"
    print "Hit Enter to use the default word list, words.txt\n\nType quit to exit the program\n\n"
    filename = raw_input("\t>>>\t")

    # ----------------------------------------------------
    # If no input, use default word list
    if filename == "":
        filename = "words.txt"
        word_list = helper_functions.load_words(filename)

    # ----------------------------------------------------
    # Return if user types quit or exit
    elif filename.lower() == "exit" or filename.lower() == "quit":
        return filename

    # ----------------------------------------------------
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

    return filename


#
#  Difficulty Selection / Hand Size Selection
#
def select_difficulty():

    hand_size = 0

    # ----------------------------------------------------
    # Ask user how many letters they want in each hand
    print variables.hr + "\t\tCHOOSE DIFFICULTY\n\nHow many letters would you like in each hand?\n"
    print "Hit Enter to use the default of 7\n\nType -1 to return to Main Menu\n\n"
    hand_size = raw_input("\t>>>\t")

    # ----------------------------------------------------
    # If no input, set number of guesses to default (10)
    if hand_size == "":
        return 7

    # ----------------------------------------------------
    # Otherwise set it to user's choice
    else:
        return int(hand_size)
