# Problem 4:
# Design a Python program that simulates a simple guessing game. The program should generate
# a random number between 1 and 100 and ask the user to guess it. Provide hints like "Too high"
# or "Too low" until the user guesses the correct number. Use a while loop for this game.

import random
# Generate a random integer between a specified range (inclusive)
upper_limit = 20
random_number = random.randint(1, upper_limit)

print(random_number)
print("I've generated a random number between 1 and", upper_limit, ". Would you dare to guess it? (I will give you some hints)...")
iterations = 0

while True:
    iterations = iterations + 1
    # print('Iteration: #',iterations, sep='')
    my_guess = int(input("Enter your guess: "))
    if my_guess == random_number:
        if iterations == 1:
            print('That is correct, you guessed it in your ', iterations,'st try.', sep='')
        elif iterations == 2:
            print('That is correct, you guessed it in your ', iterations,'nd try.', sep='')
        elif iterations == 3:
            print('That is correct, you guessed it in your ', iterations,'th try.', sep='')
        else:
            print('That is correct, you guessed it in your ', iterations,'th try.', sep='')
        break
    elif iterations < 4 and my_guess > random_number:
        print('The number you try to guess is smaller than', my_guess, )
    elif iterations < 4 and my_guess < random_number:
        print('The number you try to guess is bigger than', my_guess, )
    elif iterations == 4 and my_guess > random_number and random_number%5 == 0:
        print('The number you try to guess is smaller than', my_guess, 'but it is also dividable by 5')
    elif iterations == 4 and my_guess > random_number and random_number%5 != 0:
        print('The number you try to guess is smaller than', my_guess, 'and it is not dividable by 5')
    elif iterations == 4 and my_guess < random_number and random_number % 5 == 0:
        print('The number you try to guess is bigger than', my_guess, 'but it is also dividable by 5')
    elif iterations == 4 and my_guess < random_number and random_number % 5 != 0:
        print('The number you try to guess is bigger than', my_guess, 'and it is not dividable by 5')
    elif iterations == 5 and my_guess > random_number and random_number%3 == 0:
        print('The number you try to guess is smaller than', my_guess, 'but it is also dividable by 3')
    elif iterations == 5 and my_guess > random_number and random_number%3 != 0:
        print('The number you try to guess is smaller than', my_guess, 'and it is not dividable by 3')
    elif iterations == 5 and my_guess < random_number and random_number % 3 == 0:
        print('The number you try to guess is bigger than', my_guess, 'but it is also dividable by 3')
    elif iterations == 5 and my_guess < random_number and random_number % 3 != 0:
        print('The number you try to guess is bigger than', my_guess, 'and it is not dividable by 3')
    elif iterations == 6 and my_guess != random_number:
        print('The number you try to guess is within the range: ', max(random_number-2,0), '-', min(random_number+2,upper_limit))
    elif iterations == 7 and my_guess != random_number:
        print('I am out of hints...')
    elif iterations > 7 and my_guess != random_number:
        print('Try again!')
