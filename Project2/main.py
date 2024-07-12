'''
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.
'''

import random
number = random.randint(1, 100)
guess = 0
count = 0
while guess != number:
    count += 1
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Higher number please.")
    elif guess > number:
        print("Lower number please.") 

print(f"Correct! It took you {count} guesses.")