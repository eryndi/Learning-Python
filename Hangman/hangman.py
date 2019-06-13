#!bin/usr/python

import functions
import data


class Player:
    def __init__(self, name):
        self.name = name
        self.score = functions.get_score(name)


class Hangman:
    def __init__(self, wordList):
        self.answer = str(functions.get_random_word(wordList)).lower()
        self.residual = self.answer[:]
        self.rounds = len(self.answer)
        self.guess = "*" * self.rounds
        print("Let's play!")

    def update_guess(self, shot):
        if shot in self.residual:
            index = self.residual.index(shot)
            self.guess = self.guess[:index] + shot + self.guess[index + 1:]
            self.residual = self.residual.replace(shot, "", 1)
            print("Good guess!, ", self.guess)
        else:
            print("Sorry", shot, "is not there, try again")

    def validate_guess(self):
        print("This is your riddle: ", self.guess)
        while True:
            shot = input("What's your guess?")
            if len(shot) > 1:
                print("You can guess only one letter per round.")
                continue
            if not shot.isalpha():
                print("Your guess in not a valid character")
                continue
            else:
                return self.update_guess(shot)


def game(player):
    hangman = Hangman(functions.validate_words(data.word_list))
    for round in range(hangman.rounds):
        print("You have", hangman.rounds - round, "guess(es)", end="")
        letter = hangman.validate_guess()
    print("You run out of your guesses, it was", hangman.answer)

if __name__ == "__main__":
    print("This is game of hangman, welcome")
    # while True:
    print("State your name and make sure to use the same name as before if you want to use your previous score")
    # name = input("Name: ")
    name = "di"
    player = Player(name)
    print(player.name, player.score)
    game(player)



