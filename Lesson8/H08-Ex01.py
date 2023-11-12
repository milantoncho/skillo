#TODO Problem 1: Rewrite the following function so it is exception safe

# def get_integer_input():
#     num = int(input("Enter an integer: "))
#     return num
# number = get_integer_input()
# print("You entered:", number)


def get_integer_input():
    while 1==1:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

number = get_integer_input()
print("You entered:", number)
