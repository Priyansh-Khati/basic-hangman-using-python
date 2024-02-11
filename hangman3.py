# now have to create functionality that the user gets chances to fill the dash completely

import random
import hamgmanwordslist
import hangmanLogo

print(hangmanLogo.logo)

print("Take a look at the word list and search which word would fit in:\n")
print(hamgmanwordslist.listt)
print("\n \n")


chosen_one = random.choice(hamgmanwordslist.listt)

#for testing code:
#print(f"The choosen ord is:{chosen_one}")

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


display = []
for i in chosen_one:
    display+='_'

print(display)

# 6 stages 6 chances
maxattempts = 6
life = maxattempts
n=int(0)

while '_' in display and n<maxattempts and life>0:
    guess = input("Guess a word:").lower()
    if guess in display:
        print("You have already chosen this letter")

    elif guess in chosen_one:  # Check if the guessed letter is in the chosen word
        for i in range(len(chosen_one)):
            if chosen_one[i] == guess:
                display[i] = guess
        print(guess , " is correct word!")
        print(display)
        n= n+1

    else:
        print(guess , " is not a correct word! You lose a life")
        n= n+1
        print(stages[life])
        life=life-1

if '_' in display:
    print("You lose!")
else:
    print("You won!")

