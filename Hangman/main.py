# Hang Man Source/Main code
from asyncore import read
from helper import *
from draw import *
from random import choice
import figure

chances = 6

f = open("Hangman Game/words.txt")
words = f.read().split()
# If you want full dictionary printed (84099 words), un-comment following line of code, a.k.a line 13
# print(words)

# ORIGINAL LISTS:
# words = games + animals + coding_languages + nouns + advanced_words
# chances = 6
# print(words)

secret = choice(words)
# secret = "star"   #test
drawword(secret)
dashes = len(secret) * '-'
drawword(dashes)

# Input/Process
while chances > 0 and dashes != secret:   # '-' in dashes
    guess = input("Please guess a letter: ")
    if guess in secret:
        print("You got a letter!  That letter was " + guess)
        dashes = updatedashes(secret, dashes, guess)
        drawword(dashes)
    else: 
        chances -= 1 # chances = chances - 1
        figure.body_parts[5 - chances]()
        print("Sorry, your guess was incorrect")
        print(str(chances) + ' left')

print("Game Over.  Thanks for playing Hangman using this program!!")
if chances > 0:
  print('Congratulations!  You have won this game!')
  print("The word was: " + secret)
else:
  print("The word was: " + secret.upper()+'!!!')
