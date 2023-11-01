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

#TODO: 9. Write a function that counts the frequency of each word in a given string and returns a dictionary with the result.

import re
from collections import Counter

sample_text = ("Чл. 1."
               "(1) България е република с парламентарно управление."
               "(2) Цялата държавна власт произтича от народа. Тя се осъществява от него непосредствено и чрез органите, предвидени в тази Конституция."
               "(3) Никоя част от народа, политическа партия или друга организация, държавна институция или отделна личност не може да си присвоява осъществяването на народния суверенитет."
               "Чл. 2."
               "(1) Република България е единна държава с местно самоуправление. В нея не се допускат автономни териториални образувания."
               "(2) Териториалната цялост на Република България е неприкосновена."
               "Чл. 3."
               "Официалният език в републиката е българският."
               "Чл. 4."
               "(1) Република България е правова държава. Тя се управлява според Конституцията и законите на страната."
               "(2) Република България гарантира живота, достойнството и правата на личността и създава условия за свободно развитие на човека и на гражданското общество."
               "(3) (Нова - ДВ, бр. 18 от 2005 г.) Република България участва в изграждането и развитието на Европейския съюз."
               "Чл. 5."
               "(1) Конституцията е върховен закон и другите закони не могат да й противоречат."
               "(2) Разпоредбите на Конституцията имат непосредствено действие."
               "(3) Никой не може да бъде осъден за действие или бездействие, което не е било обявено от закона за престъпление към момента на извършването му."
               "(4) Международните договори, ратифицирани по конституционен ред, обнародвани и влезли в сила за Република България, са част от вътрешното право на страната. Те имат предимство пред тези норми на вътрешното законодателство, които им противоречат."
               "(5) Всички нормативни актове се публикуват. Те влизат в сила три дни след обнародването им, освен когато в тях е определен друг срок."
               "Чл. 6."
               "(1) Всички хора се раждат свободни и равни по достойнство и права."
               "(2) Всички граждани са равни пред закона. Не се допускат никакви ограничения на правата или привилегии, основани на раса, народност, етническа принадлежност, пол, произход, религия, образование, убеждения, политическа принадлежност, лично и обществено положение или имуществено състояние."
               "Чл. 7."
               "Държавата отговаря за вреди, причинени от незаконни актове или действия на нейни органи и длъжностни лица."
               "Чл. 8."
               "Държавната власт се разделя на законодателна, изпълнителна и съдебна.")

def words_counter(some_input_list):
    garbage_to_clean = r'[-[()\],."!\s]'
    cleaned_text = re.sub(garbage_to_clean, ' ', some_input_list)
    words = re.findall(r'\b\w+\b', cleaned_text.lower())
    resulting_dict = dict(Counter(words))
    sorted_resulting_dict = dict(sorted(resulting_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_resulting_dict)

words_counter(sample_text)



# lambda - някаква инкогнито функцийка
# ant = lambda a, b: a + b
# print("ant: ", ant(2,3))




#TODO: 10. Create two sets with some common elements and find their intersection.

set_europe = {"Norway", "Italy", "Romania"}
set_eu = {"Italy", "France", "Romania"}
for i in set_eu:
    for j in set_europe:
        if j == i:
            print(j)

print("Intersecting set: ", set_europe & set_eu)
print("Intersecting set: ", set_europe.intersection(set_eu))


#TODO: 11. Given two sets, write a function that determines if one set is a subset of the other.

set_europe = {"Norway", "Italy", "Romania","Spain","Austria"}
set_eu = {"Italy", "Romania","BG"}

def is_subset(set_small, set_big):
    return set_small.issubset(set_big)

if is_subset(set_eu,set_europe) is True:
    print("set_eu is a subset of set_europe")
    print(f"i.e. {set_eu} is a subset of {set_europe}")
else:
    print("set_eu is NOT a subset of set_europe")
    print(f"i.e. {set_eu} is a subset of {set_europe}")

#TODO:  Why are the {} reordered?