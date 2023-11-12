#TODO: 4. Write a program that reads a CSV file called "employee_data.csv,"
# and for each employee, calculates their total salary (considering base salary and bonuses)
# and saves it in a new CSV file called "total_salaries.csv."

import csv

input_file = "H09-Ex04_employee_data.csv"
output_file = "H09-Ex04_total_salaries.csv"

with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.DictReader(input_csv)
    writer = csv.writer(output_csv)

    writer.writerow(['Employee', 'TotalSalary'])

    for row in reader:
        # print(row)
        salary = float(row["Salary"])
        bonus_percentage = float(row["Bonus"].strip('%')) / 100

        employee = row["Employee"]
        totalsalary = salary + (salary * bonus_percentage)

        writer.writerow([employee, totalsalary])

print(f"{output_file} was created.")