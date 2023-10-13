# Problem 2:
# Write a Python script that prompts the user in the console a simple problem ( how much does 5
# + 17 equal to ) until the user provides a correct answer.

print('How much does 5 + 17 equal to?')
answer = 0
result = 5+17
while True:
    answer = int(input('The answer is: '))

    if answer == result:
        print("That's correct, thank you.")
        break
    else:
        print('Wrong answer. Please, try again...')


