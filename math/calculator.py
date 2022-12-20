def main():

    num1 = int(input("Enter the first number that you want to calculate: "))
    operator = input("Enter '+', '-', '*' or '/' ")
    num2 = int(input("Enter the second number that you want to calculate: "))

    #logic

    if operator == '+':
        answer = num1 + num2


    if operator == '-':
        answer = num1 - num2


    if operator == '*':
        answer = num1 * num2


    if operator == '/':
        answer = num1 / num2


    print("The answer is " + str(answer))

    rerun = input("Do you want to run again? (y/n) ").lower()
    if rerun == 'y':
     main()
    elif rerun == 'n':
     exit()
main()