
def main():
    op = input("> Would you like to find a square or cube? ")
    if op == "square" or op == "sqr":
        square = int(input("> Enter the number you would like to find the square of: "))
        sqr = square * square
        print(f"> {square} square = {sqr}")
    elif op == "cube" or op == "cu":
        cube = int(input("> Enter the number you would like to find the cube of: "))
        cu = cube * cube
        print(f"> {cube} cube = {cu}")
    repeat = input("> Would you like to run again? y/n ")
    if repeat == "y":
        main()
    elif repeat == "n":
        exit()
main()
    