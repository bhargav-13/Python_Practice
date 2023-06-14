import random

low = 1
high = 100
# options = ("rock", "paper", "scissors")
#
# number = random.randint(low, high)
# # option = random.choice(options)
#
# print(number)

guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter number between {low} - {high}: "))
    
    if guess > number:
        print(f"{guess} is too high")
    elif guess < number:
        print(f"{guess} is too low")
    else:
        print(f"---------{guess} is correct!!!!-------")

