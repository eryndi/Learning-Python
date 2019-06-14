#!bin/usr/python

import functions
import data
import pickle
from random import randrange

class Player:
    def __init__(self, name):
        self.name = name
        self.score = functions.get_score(name)
        print("Welcome", self.name, "your score:", self.score)

    def save_score(self):
        # scores = {"name": playerName, "score": 0}
        with open("scores", "rb") as file:
            pickler = pickle.Unpickler(file)
            scores = pickler.load()
            print(scores)

        scores.setdefault(self.name, self.name)
        scores[self.name] = self.score
        # scores.dump(scores)

        with open("scores", "wb") as file:
            pickler = pickle.Pickler(file)
            pickler.dump(scores)

        with open("scores", "rb") as f:
            pickler = pickle.Unpickler(f)
            foo = pickler.load()
            print(foo)


class Hangman:
    def __init__(self, wordList):
        self.answer = str(functions.get_random_word(wordList)).lower()
        self.used = []
        self.rounds = len(self.answer)
        self.riddle = "*" * self.rounds
        print("Let's play! this is your riddle", self.riddle)
        print(self.answer)

    def give_me_letter(self):
        r = None
        while r is None or r in self.used:
            r = randrange(0, len(self.answer), 1)
            print(r)
        self.used.append(r)
        self.update_riddle(r)

    def guess_answer(self, round):
        if input("Type your guess:").lower() == self.answer:
            score = self.rounds - round
            player.score += score
            print("Congratulations you won! You scored", score, "points, your all time total is", player.score)
            return True
        else:
            return False

    def update_riddle(self, index):
        self.riddle = self.riddle[:index] + self.answer[index] + self.riddle[index + 1:]


def game(player):
    hangman = Hangman(functions.validate_words(data.word_list))
    for round in range(hangman.rounds):
        print("You have", hangman.rounds - round, "guess(es)", end="")
        guessAnswer = input("Do you want to guess the answer? [y/n]").lower()
        if guessAnswer == "y":
            if hangman.guess_answer(round) is True:
                break;
            else:
                continue;
        else:
            hangman.give_me_letter()
        print("This was your riddle:", hangman.riddle)



if __name__ == "__main__":
    print("This is game of hangman, welcome")
    # while True:
    print("State your name and make sure to use the same name as before if you want to use your previous score")
    # name = input("Name: ")
    name = "di"
    player = Player(name)
    print(player.name, player.score)
    while True:
        game(player)
        restartGame = input("Would you like to start a new game? [y/n]").lower()
        if restartGame == "y":
            True
        else:
            player.save_score()
            print("Your score is saved")
            print("Quiting game...")
            break;



