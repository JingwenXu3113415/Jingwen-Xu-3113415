# Jingwen Xu-3113415  
final project for Seminar KI in der Logistik - Programmierung WiSe 22/23  
# Name of the project  
  Guess the Number Game  
# Main Process-Purpose    
  Generate a random number between 1 and 100.   
  Ask the user to guess the number,receive user input, then tell them whether they guessed too low, too high, until the user guessed the correct answer.  
  Generate an option for user can quit the game at any time.  
  Keep track of how many guesses the user has taken, and when the game ends, print this out.  
# Process in detail- program
  #Import the random module  
    import random  
  #Create a number as random number, define guess as the variable guess number and count as record cycle times  
    number = random.randint(1, 100)  
    guess = 0  
    count = 0  
   #Use the while statement to create a loop, and use the input function to receive the number entered by the user  
    while guess != number and guess != "exit":  
    guess = input("Please guess a number between 1 and 100. When you want to end the game print 'exit': ")  
   #Use the if statement to create an end condition for the loop  
    if guess == "exit":  
        print("Game Over")  
        break  
    #Use the int function to convert the received user input value into an integer type, and calculate the number of guesses  
    guess = int(guess)  
    count += 1  
    #Use the if...elif...else statement to determine whether the number is in the corresponding range, whether it is too large or too small  
    if guess not in range(1, 100):  
        print("You have to guess a number between 1 and 100!")  
    elif guess < number:  
        print("You've guessed too low!")  
    elif guess > number:  
        print("You've guessed too high!")  
    else:  
        print("You've got it! It took you {} tries!".format(count))  
        break  
      #Add the input function to wait for the user to enter any key before exiting the program  
      input("Please enter any key to exit")  
