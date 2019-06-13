# !bin/usr/python3

import os
import pickle
from random import randrange

def get_score(playerName):
    """loads pickled scores file

    if file doesn't exist it is created
    :return scores_file
    """
    if os.path.exists("scores"):
        with open("scores", "rb") as file:
            depickler = pickle.Unpickler(file)
            scores = depickler.load()
            return scores.get(playerName, 0)

    else:
        scores = {"name": playerName, "score": 0}
        with open("scores", "wb") as file:
            pickler = pickle.Pickler(file)
            pickler.dump(scores)
            return 0


def update_scores(playerName):
    """update scores file before quit"""



def store_file(file):
    """store pickled file"""

    pass


def get_random_word(wordList):
    index = randrange(1, len(wordList), 1)
    return (wordList[index])


def validate_words(wordList, char_max=8):
    """A word can have max 8 characters

    returns a cleared list of words
    """
    try:
        wordList = [word for word in wordList if len(word) < 9]
    except ValueError:
        print("word list is in wrong format")

    return wordList;


def calculate_score():
    """Calculates score for player

    :return:
    """
    pass

def get_player(PlayerName):
    """
    get player name from file
    :return str name    """
