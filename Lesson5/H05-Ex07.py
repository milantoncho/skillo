#TODO: 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank accounts.


students_accounts = {}
# students_accounts["Ant"]=[]
# students_accounts["Ant"].append(123)  # Add a single value
# students_accounts["Ant"].append(321)  # Add a single value
# students_accounts["Ant"].extend([234, 345])


def add_student(some_student_name):
    students_accounts[some_student_name]=[]
    return students_accounts[some_student_name]

def add_accounts(some_student_name, some_account_number):
    add_student(some_student_name)
    students_accounts[some_student_name].append(some_account_number)
    return students_accounts[some_student_name]


def add_student_account(student_id, *accounts):
    global students_accounts

    if student_id not in students_accounts:
        students_accounts[student_id] = {}

    if accounts:
        students_accounts[student_id]["accounts"] = list(accounts)


# Example usage:
add_student_account("Ant")
add_student_account("Tom", 85)
add_student_account("Kym", 90, 92, 88)

# Print the resulting dictionary
print(students_accounts)

#
# # #TODO: 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank accounts.
#
#
# students_accounts = {}
#
# def add_student(some_student_name):
#     if some_student_name in students_accounts:
#         pass
#         # print("This student already has an account")
#     else:
#         students_accounts[some_student_name]=[]
#     return students_accounts[some_student_name]
#
# def add_accounts(some_student_name, some_account_number):
#     add_student(some_student_name)
#     students_accounts[some_student_name].append(some_account_number)
#     return students_accounts[some_student_name]
#
# add_student("Ant")
# print(students_accounts)
#
# add_accounts("Ant","123")
# print(students_accounts)
#
# add_accounts("Ant","234")
# print(students_accounts)