#TODO: 2. Write a program that reads a text file, "words.txt," and counts the number of words in it

filename = "words.txt"

with open(filename, 'r') as my_file:
    words_count = my_file.read().split()

    print("There are", len(words_count), "words in file", filename)
