# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
import variables


def load_words(filename):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print variables.hr + "\t\tLoading word list from file..."
    # inFile: file
    inFile = open(filename, 'r', 0)
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = string.split(line)
    print " \n\t\t", len(word_list), "words loaded from " + filename
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------
