#TODO 7. Create a CSV file, "student_data.csv," with student names and their corresponding JSON data
# containing exam scores. Write a program that reads the CSV file and calculates the average score for each student.



import csv
import json
from collections import defaultdict

json_file = "H09-Ex07_json_input.json"
output_file = "H09-Ex07_average_scores.csv"

with open(json_file, 'r') as file:
    json_data = json.load(file)


student_scores = defaultdict(list)
for row in json_data:
    student_scores[row["Student"]].append(float(row["Score"]))

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Average Score"])

    for name, scores in student_scores.items():
        average_score = round(sum(scores) / len(scores),2)
        writer.writerow([name, average_score])

print(f"Results written to {output_file}")




# a={}
# for j in range(5):
#     a[j]=j
# print("dict:",a)
#
# b=[]
# for k in range(5):
#     b.append(k)
# print("list:",b)
#
# c = defaultdict(list)
# for i in range(5):
#     c[i].append(i)
#
# print("Dictionary with values as list:")
# print(c)