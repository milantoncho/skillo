#TODO: 14. Given a list of words, create a dictionary where the keys are the words and the values are their lengths, using dictionary comprehension.

my_list2 = ["Alfa","Beta","Beta","Gamma","Delta"]
def list_to_dict(some_list):
    d = {}
    for i in some_list:
        d[i] = len(i)
    return d
print(list_to_dict(my_list2))