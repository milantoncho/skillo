# Problem 3:
# Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is
# divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.

print('Define a [from-to] range, to play around with 3 and 5')
rs = 0

from_number = int(input('Enter the "from" number: '))
while True:
    to_number = int(input('Enter the "to" number: '))

    if to_number > from_number:
        break
    else:
        print('The "to" number [', to_number, '] is not greater than the "from" number [',from_number , '].')

for i in range(from_number, to_number + 1):
    if i%3 == 0 and i%5 == 0:
        print(i, 'FizzBuzz')
    elif i%3 == 0:
        print(i, 'Fizz')
    elif i%5 == 0:
        print(i, 'Buzz')
    else:
        pass

