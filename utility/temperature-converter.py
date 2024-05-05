def main():

    conversion = input("Would you like to convert from C to F or from F to C? ")


    if conversion == "C to F":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print (fahrenheit)
    else:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit - 32 * 5/9
        print(celsius)

    repeat = input("Would you like to convert again? y/n: ")

    if repeat == "y":
        main()
    elif repeat == "n":
        exit()

main()
