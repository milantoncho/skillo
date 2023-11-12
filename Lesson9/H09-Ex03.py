#TODO 3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores this data in a CSV file called "student_scores.csv."

import csv
import os

datafile = "H09-Ex03_student_scores.csv"
header = ['FirstName', 'LastName', 'Subject', 'Score']
data = []

print("Please, input the students data")
data.append(input("First Name: "))
data.append(input("Last Name: "))
data.append(input("Subject: "))
data.append(int(input("Score: ")))

file_exists = os.path.isfile(datafile)

if file_exists is True:
    with open(datafile, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
else:
    with open(datafile, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerow(data)

