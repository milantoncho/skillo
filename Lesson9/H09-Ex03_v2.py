#TODO 3. Create a Python script that prompts the user to enter student names and their corresponding scores, then stores this data in a CSV file called "student_scores.csv."


import csv
import os

datafile = "H09-Ex03_student_scores_v2.csv"
header = ['FirstName', 'LastName', 'Subject', 'Score']

def input_student_data():
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
    next_actions()

def read_csv_data(some_csv_file):
    with open(some_csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(','.join(row))
    next_actions()

def next_actions ():
    next_action = 3
    while next_action not in (1, 2, 0):
        next_action = int(input("\nWhat would you like to do next?\n"
                                "1 - review the studetns score\n"
                                "2 - add new student\n"
                                "0 - exit\n"
                                "Your choice: "))
        if next_action == 1:
            read_csv_data(datafile)
        elif next_action == 2:
            input_student_data()
        elif next_action == 0:
            print("Exiting...")
            break


next_actions()