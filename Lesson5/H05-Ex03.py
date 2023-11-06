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