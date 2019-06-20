# HANGMAN

## Functional definition:
Hangman is a game where player plays against computer trying to guess a max 8 character-long random word. 
Each round player gets a random letter of the guessed word against one point less to win or a chance to guess the word. 
Total points to win is match number of letters in a word. Player has as many guesses as there are letters in a guessed word.

Wrong guess means a lost game. Player can play as many games as she wishes, score is stored as well as username to retake later. 


## User story:
1. player is asked his name, if there is a username matching, player continues to add to previous score. 
If not, score starts at 0.
2. computer takes random word from a list of 8-letter words 
3. computer counts a total of turns to guess a name which equals to max points to win
4. player guess one letter per turn (checked by computer)
3. each player find a correct character computer displays already found letters including the most recent one.  
Missing characters is anonymized as asterisks *
4. Player has as many turns to guess a word as there is characters in a word.
5. If player uesd all his turns he lost and he is hanged
. Player's score is calculated of total unused turns to guess a word
data.py -> contains variables needed for the game; word list, number of chances, ...
functions.py -> contains app functions
hangman.py -> contains the game

scores -> file contains dictionary of scores
- if the file doesn't exist  program creates one
- if player is not already in dictionary, he is added with score 0 
 