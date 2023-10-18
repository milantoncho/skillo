# Problem 3: Temperature Conversion
# Write a program that converts temperatures between Celsius and Fahrenheit. Create two
# functions, one for each conversion, and use them in a program to convert temperatures
# provided by the user.


def convert_fahrenheit_to_celsius(fahr):
    cel = round((fahr-32)*5/9,1)
    return cel

def convert_celsius_to_fahrenheit(cel):
    fahr = round((cel*9/5)+32,1)
    return fahr

temp = scale = False
while True:
    input_values = input("Enter temperature (e.g. 95 F or 23 C) to get a converted value: ")
    if ' ' in input_values:
        temp, scale = input_values.split()
        if scale.upper() in ["F", "C"] and temp.isdigit() is True:
            break

if scale.upper() == "F":
    print(temp, "degrees in Fahr are equal to", convert_fahrenheit_to_celsius(int(temp)), "in Cel")
else:
    print(temp, "degrees in Cel are equal to", convert_celsius_to_fahrenheit(int(temp)), "in Fahr")


#########################################################################################################
#
# def convert_fahrenheit_to_celsius(fahr):
#     cel = round((fahr-32)*5/9,1)
#     return cel
#
# def convert_celsius_to_fahrenheit(cel):
#     fahr = round((cel*9/5)+32,1)
#     return fahr
#
# temp = scale = False
# # scale = False
# while scale.upper() not in ["F", "C"] or temp.isdigit() is False:   #or ' ' in input_values:
#     input_values = input("Enter temperature (e.g. 95 F or 23 C) to get a converted value: ")
#     temp, scale = input_values.split()
#
#
# if scale.upper() == "F":
#     print(temp, "degrees in Fahr are equal to", convert_fahrenheit_to_celsius(int(temp)), "in Cel")
# else:
#     print(temp, "degrees in Cel are equal to", convert_celsius_to_fahrenheit(int(temp)), "in Fahr")
#
###################################################################################################

# def convert_fahrenheit_to_celsius(fahr):
#     cel = round((fahr-32)*5/9,1)
#     return cel
# print("Temp is Cel: ", convert_fahrenheit_to_celsius(float(input("Temp in Fahr: "))))
#
#
# def convert_celsius_to_fahrenheit(cel):
#     fahr = round((cel*9/5)+32,1)
#     return fahr
# print("Temp is Fahr: ", convert_celsius_to_fahrenheit(float(input("Temp in Cel: "))))