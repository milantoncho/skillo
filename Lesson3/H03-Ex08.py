# Problem 8: Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested
# for loops:
# Expected output for input 5:
# 1
# 12
# 123
# 1234
# 12345

inum=int(input("Enter a number: "))
for i in range (1,inum+1):
    for j in range (1, i+1):
        print (j,end='')
    print('')