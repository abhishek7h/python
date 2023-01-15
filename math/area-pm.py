def bruh():
    toFind = 'area', 'perimeter'
    print(toFind)
    query1 = str(
        input('Enter whether you would like to check area or perimeter: '))
    if query1 == 'area':
        shapesArea = "rect", "circ", "tri", "sqr"
        print(shapesArea)
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
    elif query1 == "perimeter":
        shapesPM = "rect", "circ", "tri", "sqr"
        print(shapesPM)
        query2 = str(
            input("Enter the shape of which you would like to find the perimeter of: "))
        if query2 == "rect":
            l = int(input("Enter length: "))
            b = int(input("Enter breadth: "))
            pm = l + b + l + b
            print("The perimeter of the rectangle is", pm)
        elif query2 == "circ":
            r = int(input("Enter radius: "))
            pi = 22/7
            pm = 2 * pi * r
            print("The circumference of the circle is", pm)
        elif query2 == "tri":
            a = int(input("Enter first side: "))
            b = int(input("Enter base: "))
            c = int(input("Enter third side: "))
            pm = a + b + c
            print("Perimeter of the triangle is", pm)
        elif query2 == "sqr":
            a = int(input("Enter side: "))
            pm = 4 * a
            print("Perimeter of the square is", pm)

    repeat = str(input("Would you like to run again? (y/n): "))
    if repeat == "y":
        bruh()
    elif repeat == "n":
        exit()


bruh()
