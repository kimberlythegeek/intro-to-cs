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
    print variables.hr + "\t\tLoading word list from file..."
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