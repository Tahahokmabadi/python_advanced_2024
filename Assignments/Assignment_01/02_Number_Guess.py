import random

number = 1 # random.randint(1, 100)
min_value = 0
max_value = 101

while True:
    guess = input(f"Enter a number between {min_value} and {max_value}:\t")
    if not guess.isdigit():
        print("Enter numbers only.")
        continue
        
    guess = int(guess)
        
    if not max_value > guess > min_value:
        print(f"You should Enter a number between {min_value} and {max_value}.")
        continue
    
    if guess == number:
        print("You've guessed correctly!")
        break
    elif guess > number:
        print("Guess a lower number!")
        max_value = guess
    else:
        print("Guess a higher number!")
        min_value = guess
