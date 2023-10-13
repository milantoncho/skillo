# Problem 1:
# Write a Python program to find the sum of all even numbers from 1 to 100 using a loop. Make
# use of control flow constructs like the for loop and conditional statements.


print('Define a [from-to] range, to calculate the sum of the even numbers within that range')
rs = 0

from_number = int(input('Enter the "from" number: '))
while True:
    to_number = int(input('Enter the "to" number: '))

    if to_number > from_number:
        break
    else:
        print('The "to" number [', to_number, '] is not greater than the "from" number [',from_number , '].')

for i in range(from_number, to_number + 1):
    if i%2 == 0:
        rs=rs+i

print('The sum of the even numbers between', from_number, 'and', to_number, 'is:', rs)


