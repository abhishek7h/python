a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b*b - 4 * a * c

if discriminant >= 0:
    print(f"The discriminant is {discriminant}, and it is a real root.")
else:
    print(f"The discriminant is {discriminant}, but it is not a real root.")
