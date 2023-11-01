# #TODO: 1. Create a list with the numbers from 1 to 10 and print it.
# def print_list(limit):
#     number_list = list(range(1, limit+1))
#     # print(number_list)
#     # for i in number_list:
#     #     print(i)
#     return number_list
#
#
# print(print_list(11))
# # print_list(11)
#
# #TODO: 1.1. Create a list with the numbers from 1 to 1000 and print it.
#
# # print(print_list(100))
#
#
# #TODO: 2. Reverse the order of the elements in the list from problem 1 and print the result.
#
# # print(print_list(10).reverse())  #Why is this failing?
# rev = print_list(10)
# rev.reverse()
# print(rev)
#
#
# #TODO 3. Given a list of words, create a new list containing the lengths of each word.
#
# family_name = ["Pacino", "Washington", "Penn", "Schwarzenegger", "Oz", "Roth"]
# def list_items_len (some_list):
#     family_name_len = []
#     for names in some_list:
#         family_name_len.append(len(names))
#     return family_name_len
#
# print(family_name)
#
# print(list_items_len(family_name))
#
#
# #TODO: 3.1. Given a list of words, create a new dictionary mapping every word to it's length.
# def list_to_dict(some_list):
#     d = {}
#     for index, name in enumerate(some_list):
#         d[index] = name
#     return d
#
#
# print(list_to_dict(family_name))
#
#
# #TODO: 4. Write a function that takes a list and returns the sum of all even numbers in the list.
#
# list_of_numbers = [44, 46, 111, 2, 23, 45, 53, 22, 230, -300]
#
# def sum_of_even_numbers(some_list_of_numbers):
#     result = 0
#     for i in list_of_numbers:
#         if i%2==0:
#             result = result+i
#         else:
#             continue
#     return result
#
# print("The sum of all even numbers from 'list_of_numbers' is:", sum_of_even_numbers(list_of_numbers))
#
#
# #TODO: 5. Given a tuple of integers, find the maximum and minimum values without using built-in functions.
# tuple_of_numbers = (33, 44, 1, 17, 25, 43)
# def min_and_max(some_tuple_of_numbers):
#     maxvalue=float("-inf")
#     minvalue=float("inf")
#     for i in some_tuple_of_numbers:
#         if i > maxvalue:
#             maxvalue = i
#         elif i < minvalue:
#             minvalue = i
#         else:
#             continue
#     return minvalue, maxvalue
# minv, maxv = min_and_max(tuple_of_numbers)
# print("Min:", minv, "Max:", maxv)
#
#
# #TODO: 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue`.
#
# queue = []
#
# def enqueue(some_element):
#     queue.append(some_element)
#
# def dequeue():
#     queue.pop(0)
#
# def control():
#     next_action = 1
#     while next_action != 0:
#         next_action = int(input('\n'
#                 '1 - Add\n'
#                 '2 - Remove\n'
#                 '3 - View Content\n'
#                 '4 - View Length\n'
#                 '0 - Exit\n'
#                 'Choose what to do with the object "queue": '))
#         if next_action == 1:
#             enqueue(input("Add: "))
#         elif next_action == 2:
#             dequeue()
#         elif next_action == 3:
#             print("The current queue content is: ", queue)
#         elif next_action == 4:
#             print("The current queue length is: ", len(queue))
#         elif next_action == 0:
#             print("Exiting...")
#
# print("start")
# control()

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
add_student_account(1)
add_student_account(2, 85)
add_student_account(3, 90, 92, 88)

# Print the resulting dictionary
print(students_accounts)



# # print(add_student("Ant"))
# name=input("Name: ")
# iban=input("IBAN: ")
# print(students_accounts)
# print(add_accounts(name,iban))
# print(students_accounts)
# iban=input("IBAN: ")
# print(add_accounts(name,iban))
# print(students_accounts)