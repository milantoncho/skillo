# Problem 5:
# Modify problem 2 so that every time the user is prompted the problem is different. Think of a
# way to design that and come up with a proper solution for that.

import random
random_number1 = random.randint(1, 20)
random_number2 = random.randint(1, 20)

if random_number1%2 == 0:
    print('How much does', random_number1, '+', random_number2, 'equal to?')
    result = random_number1 + random_number2
else:
    print('How much does', random_number1, '*', random_number2, 'equal to?')
    result = random_number1 * random_number2
answer = 0

while True:
    answer = int(input('The answer is: '))

    if answer == result:
        print("That's correct, thank you!")
        break
    else:
        print('Wrong answer. Please, try again...')