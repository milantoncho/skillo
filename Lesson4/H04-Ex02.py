# Problem 2: Area of Shapes
# Create a module named `geometry` with functions to calculate the area of common shapes like
# a square, rectangle, triangle, and circle. Import this module and use it to calculate the areas of
# different shapes.


def area_square(side):
    area = side**2
    return area

def area_rectangle(sideA, sideB):
    area = round(sideA*sideB,2)
    return area

def area_triangle(base, height):
    area = round(base*height/2,2)
    return area

def area_circle(radius):
    import math
    area = round(math.pi * radius ** 2, 2)
    return area

def geometry(intput):
    if intput == "1":
        print ("The area of the square is", area_square(int(input("Enter the square's side: "))))
    elif intput == "2":
        print ("The area of the rectangle is", area_rectangle(int(input("Enter the rectangle's sideA: ")),int(input("Enter the rectangle's sideB: "))))
    elif intput == "3":
        print ("The area of the triangle is", area_triangle(int(input("Enter the triangle's base: ")),int(input("Enter the triangle's height: "))))
    elif intput == "4":
        print ("The area of the circle is", area_circle(int(input("Enter the circle's radius: "))))
    else:
        pass
    return intput

print("Area of what would you like to calculate?")
print("1 - the area of a Square")
print("2 - the area of a Rectangle")
print("3 - the area of a Triangle")
print("4 - the area of a Circle")

option = False
while option not in ["1", "2", "3", "4"]:
    option=(input("Select a valid options, [1-4]: "))
geometry(option)
