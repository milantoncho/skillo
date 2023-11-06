#TODO: 5. Given a tuple of integers, find the maximum and minimum values without using built-in functions.
tuple_of_numbers = (33, 44, 1, 17, 25, 43)
def min_and_max(some_tuple_of_numbers):
    maxvalue=float("-inf")
    minvalue=float("inf")
    for i in some_tuple_of_numbers:
        if i > maxvalue:
            maxvalue = i
        elif i < minvalue:
            minvalue = i
        else:
            continue
    return minvalue, maxvalue
minv, maxv = min_and_max(tuple_of_numbers)
print("Min:", minv, "Max:", maxv)