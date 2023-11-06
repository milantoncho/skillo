#TODO: 1. Create a Python script that reads a text file called "numbers.txt" containing integers and calculates their sum.

filename = "numbers.txt"
a=0

with open(filename, 'r') as my_file:
    lines = my_file.readlines()
    for line in lines:
        a = a + int(line)
    print(a)