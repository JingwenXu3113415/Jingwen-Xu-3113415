import random

number = random.randint(0,100)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("please guess a nmber between 1 and 100. when you want to end the game print 'exit':")
    if guess == "exit":
        print("game over")
        break
    guess = int(guess)
    count += 1
    if guess not in range(1,100):
        print("You have to guess a number between 1 and 100!")
    elif guess < number:
        print("You've guessed too low!")
    elif guess > number:
        print("You've guessed too high!")
    else:
        print("You've got it! It took you {} tries!".format(count))
        break
