# Problem 0:
# Complete the following function so that it returns the sum of the elements in the list passed as
# an argument
# def sum_elements(arr):
# result = 0
# #insert code here
# return result
# # Tests
# print(sum_elements([1,2,3,4])
# print(sum_elements([0])
# print(sum_elements([])
# print(sum_elements([-1, 1])

# list = [1, 2, 3]
# for i in list:
#     print (list[i-1])
# for i in range(len(list)):
#     print (list[i])


def sum_elements(arr):
    result = 0
    for i in range(len(arr)):
        result = result + arr[i]
    return result

user_input = input("Enter a list of numbers separated by spaces: ")
mylist = list(map(int, user_input.split()))
print (sum_elements(mylist))

print (sum_elements([1, 2, 20, 21]))


