#TODO: 1. Create a list with the numbers from 1 to 10 and print it.
def print_list(limit):
    number_list = list(range(1, limit+1))
    # print(number_list)
    # for i in number_list:
    #     print(i)
    return number_list


print(print_list(11))
# print_list(11)

#TODO: 1.1. Create a list with the numbers from 1 to 1000 and print it.

# print(print_list(100))


#TODO: 2. Reverse the order of the elements in the list from problem 1 and print the result.

# print(print_list(10).reverse())  #Why is this failing?
rev = print_list(10)
rev.reverse()
print(rev)


#TODO 3. Given a list of words, create a new list containing the lengths of each word.

family_name = ["Pacino", "Washington", "Penn", "Schwarzenegger", "Oz", "Roth"]
def list_items_len (some_list):
    family_name_len = []
    for names in some_list:
        family_name_len.append(len(names))
    return family_name_len

print(family_name)

print(list_items_len(family_name))


#TODO: 3.1. Given a list of words, create a new dictionary mapping every word to it's length.
def list_to_dict(some_list):
    d = {}
    for index, name in enumerate(some_list):
        d[index] = name
    return d



print(list_to_dict(family_name))