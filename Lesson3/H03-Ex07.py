# Problem 7:
# Create a Python program that checks if a given integer is a prime number. Use a for loop to
# iterate through possible divisors and use an if-else statement to determine if it's prime.

inum=int(input("Enter a number: "))
list = [2,3,5]
prime = 0
for i in list:
    if inum%i == 0 and inum != 2 and inum != 3 and inum != 5:
        print(inum, 'is not a prime number as it can be divided by', i, '>>>',int(inum/i))
        prime = 0
        break
    else:
        prime = prime+1
if prime>0:
    print (inum, 'is a prime number')