# HANGMAN

1. Player is asked his name, his score is stored. 
Score starts at 0.
2. computer takes randomly word from a list of 8-letter words 
3. computer counts a total of turns to guess a name
4. player guess one letter per turn (checked by computer)
3. if player found a correct character computer displays already found letters including the most recent one.  
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
 