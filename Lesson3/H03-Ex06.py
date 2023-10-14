# Problem 6:
# Write a Python program that takes an integer input from the user and prints the multiplication
# table for that number from 1 to 10 using a for loop.

ranf = 15
rant = 35
valid_number = False
while valid_number is False:
    inum = int(input(f"Enter a number between {ranf} and {rant}: "))
    if ranf <= inum <= rant:
        for i in range(1,11):
            print(inum, "multiplied by", i, "is:", inum*i)
        valid_number = True
    else:
        print(inum, "is outside the specified range. Try again.")