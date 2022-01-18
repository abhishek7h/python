num1 = int(input("Enter the first number that you want to calculate: "))
num2 = int(input("Enter the second number that you want to calculate: "))
operator = (input("Enter either [+, -, * or /] "))

if operator == '+' :
    print(num1 + num2)
    
    
elif operator == '-' :
    print(num1 - num2)
    
    
elif operator == '*' :
    print(num1 * num2)
    
    
elif operator == '/' : 
    print(num1 / num2)