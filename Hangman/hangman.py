#!bin/usr/python

import functions
import data



if __name__ == "__main__":
    print("This is game of hangman, welcome")
    while True:
        print("State your name and make sure to use the same name as before if you want to use your previous score")
        name = input("Name: ")
        scores = functions.get_scores(name)
        print(scores)





