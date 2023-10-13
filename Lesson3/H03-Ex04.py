# Problem 4:
# Design a Python program that simulates a simple guessing game. The program should generate
# a random number between 1 and 100 and ask the user to guess it. Provide hints like "Too high"
# or "Too low" until the user guesses the correct number. Use a while loop for this game.

import random
random_number = random.randint(1, 10)
# print(random_number)
print("I've generated a random number between 1 and 10. Would you dare to guess it? (I might give you some hints)")

while True:
    my_guess = int(input())
    if my_guess == random_number:
        print('That is correct')
        break
    elif my_guess > random_number:
        print ('The number you try to guess is smaller than', my_guess, 'Try again:')
    else:
        print ('The number you try to guess is bigger than', my_guess, 'Try again:')

########################################################################################################################

# import random
# random_number = random.randint(1, 10)
# # print(random_number)
# print("I've generated a random number between 1 and 10. Would you dare to guess it? (I might give you some hints)")
# correct_guess = False
# while correct_guess is False:
#     my_guess = int(input())
#     if my_guess == random_number:
#         print('That is correct')
#         correct_guess = True
#     elif my_guess > random_number:
#         print ('The number you try to guess is smaller than', my_guess, 'Try again:')
#     else:
#         print ('The number you try to guess is bigger than', my_guess, 'Try again:')

########################################################################################################################

# import random
# random_number = random.randint(1, 10)
# # print(random_number)
# print("I've generated a random number between 1 and 10. Would you dare to guess it? (I might give you some hints)")
#
# my_guess = int(input())
# while my_guess != random_number:
#     if my_guess > random_number:
#         print ('The number you try to guess is smaller than', my_guess, 'Try again:')
#     else:
#         print ('The number you try to guess is bigger than', my_guess, 'Try again:')
#     my_guess = int(input())
# print('That is correct')
