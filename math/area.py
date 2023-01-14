options = "rect", "circ", "tri"
print(options)
query = str(
    input("Enter the shape of which you would like to find the area of: "))
if query == "rect":
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    area = l * b
    print("The area of the rectangle is", area)
elif query == "circ":
    r = int(input("Enter radius: "))
    pi = 3.14
    area = pi * r * r
    print("The area of the circle is", area)
elif query == "tri":
    a = int(input("Enter base: "))
    h = int(input("Enter height: "))
    area = a * h / 2
    print("The area of the triangle is", area)
else:
    print("Invalid input")
