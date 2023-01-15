def bruh():
    ''' option = 'area', 'perimeter'
    print(option)
    queryy = str(input('Enter whether you would like to check area or perimeter: ')) '''
    options = "rect", "circ", "tri", "sqr"
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
        b = int(input("Enter base: "))
        h = int(input("Enter height: "))
        area = b * h / 2
        print("The area of the triangle is", area)
    elif query == "sqr":
        s = int(input("Enter  side: "))
        area = s * s
        print("The area of the square is", area)

    else:
        print("Invalid input")
    repeat = str(input("Would you like to run again? (y/n): "))
    if repeat == "y":
        bruh()
    elif repeat == "n":
        exit()


bruh()
