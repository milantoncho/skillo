# Problem 1: Simple Calculator Function
# Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*',
# or '/') as arguments and returns the result of the operation.

def validation_num(arg):
    while arg not in range(-100, 101):
        arg = int(input("Enter a valid number, being within the range(-100, 101): "))
    return arg

def validation_op(operator):
    while operator not in ["+", "-", "*", "/"]:
        operator = input("Enter a valid operator (+, -, *, /):")
    return operator

def simple_calculator(argument1, oper, argument2):
    if oper == "+":
        return argument1 + argument2
    elif oper == "-":
        return argument1 - argument2
    elif oper == "*":
        return argument1 * argument2
    elif oper == "/":
        return argument1 / argument2

arg1 = validation_num(int(input("First number: ")))
op = validation_op(input("Operator: "))
arg2 = validation_num(int(input("Second number: ")))

print("The result is:", simple_calculator(arg1, op, arg2))
