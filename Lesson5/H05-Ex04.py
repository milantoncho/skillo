#TODO: 4. Write a function that takes a list and returns the sum of all even numbers in the list.

list_of_numbers = [44, 46, 111, 2, 23, 45, 53, 22, 230, -300]

def sum_of_even_numbers(some_list_of_numbers):
    result = 0
    for i in list_of_numbers:
        if i%2==0:
            result = result+i
        else:
            continue
    return result

print("The sum of all even numbers from 'list_of_numbers' is:", sum_of_even_numbers(list_of_numbers))
