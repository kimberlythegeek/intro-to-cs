import os.path
import helper_functions
import functions
import variables

filename = ""
hand_size = 0

# ----------------------------------------------------
# While the user has not exited
while True:

    # File Selection
    filename = functions.select_file()

    # ----------------------------------------------------
    # Break if user types quit or exit
    if filename.lower() == "exit" or filename.lower() == "quit":
        break


    word_list = helper_functions.load_words(filename)

    # Difficulty Selection (Hand Size Selection)
    hand_size = functions.select_difficulty()

    # While user has not exited
    while hand_size >= 0:
        print "hand size: " + str(hand_size)
        break





