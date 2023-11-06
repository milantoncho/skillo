#TODO: 12. Write a function to remove duplicates from a list using a set.

my_list = ["Alfa","Beta","Beta","Gamma","Delta"]

def no_duplicates_list (some_input_list):
    temp_set = set()
    for i in some_input_list:
        temp_set.add(i)
    output_list = list(temp_set)
    return output_list

print("input list: ", my_list)
print("output_list: ", no_duplicates_list(my_list))