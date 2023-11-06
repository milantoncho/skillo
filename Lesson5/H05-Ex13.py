#TODO: 13. Use list comprehension to create a list of the squares of even numbers from 1 to 30.

squares_of_evens = [x**2 for x in range(1, 31) if x % 2 == 0]

# squares_of_evens = []
# for x in range(1, 31):
#     if x % 2 == 0:
#         squares_of_evens.append(x**2)

print("Squares of evens between 1 and 30", squares_of_evens)