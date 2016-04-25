import variables


# ----------------------------------------------------
# Opening screen and file selection

def select_file():

    print variables.hangman

    # Get file name for word list from user
    print variables.hr + "Enter the full file name of the word list you would like to use\n"
    print "Hit Enter to use the default word list, words.txt\n\nType quit to exit the program\n\n"
    filename = raw_input("\t>>>\t")

    return filename


# ----------------------------------------------------
# Check to see if all letters in the word have been guessed

def word_guessed(word, found_list):
    i = 0
    # Check to see if word has been guessed
    for char in word:
        if not found_list[i]:
            return
        i += 1
    print '\nword solved!\n'
    solved = True
    return solved


# ----------------------------------------------------
# Check to see if the user has already used this letter
# Will not deduct guesses for a wrong letter entered more than once


def already_used_letter(guess, list_of_guesses, alphabet):
    for char in list_of_guesses:
        if guess == char:
            return True

    # If not already used, remove letter from alphabet list to show user what letters are left
    list_of_guesses.append(guess)
    remove_letter(guess, alphabet)
    return False


# ----------------------------------------------------
# Remove letter from alphabet list to show user what letters are left

def remove_letter(guess, alphabet):
    i = 0
    for character in alphabet:
        if guess == character:
            alphabet[i] = " "
            return
        i += 1


# ----------------------------------------------------
# Check to see if letter is in the word

def check_guess(word, guess, num_guesses, character_list, found_list, progress_list):
    guess_flag = False
    i = 0
    print variables.hr

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


# ----------------------------------------------------
# print "animation"

def print_hangman(num_guesses):
    if num_guesses > 5:
        print variables.hangman_picture_6
    elif num_guesses == 5:
        print variables.hangman_picture_5
    elif num_guesses == 4:
        print variables.hangman_picture_4
    elif num_guesses == 3:
        print variables.hangman_picture_3
    elif num_guesses == 2:
        print variables.hangman_picture_2
    elif num_guesses == 1:
        print variables.hangman_picture_1


# ----------------------------------------------------
# End game if player lost
def lost_game(solved, num_guesses, word):
    if not solved and num_guesses == 0:
        print variables.hr + variables.hangman_picture_0 + "\n\n you lost :( out of guesses\n\n"
        print "\n\n\tThe word was: " + word.upper()
        return True
    else:
        return False

