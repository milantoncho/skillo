#TODO: Problem 2: Research and understand how does selections sort work. Debug and fix the following code to make it correct

# def selection_sort(arr):
#     for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#     if arr[i] < arr[min_index]:
#     min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

my_list = [44, 29, 12, 8, 11]
selection_sort(my_list)
print(selection_sort(my_list))