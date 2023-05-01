import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

quadraticFormulaPlus = -b + math.sqrt(b*b - 4*a*c)/2*a
quadraticFormulaMinus = -b - math.sqrt(b*b - 4*a*c)/2*a
qfp2 = quadraticFormulaPlus/2
qfm2 = quadraticFormulaMinus/2
# qfp22 = qfp2/2
# qfm22 = qfm2/2


print(f"The roots are {quadraticFormulaPlus} and {quadraticFormulaMinus}.")

if quadraticFormulaPlus % 2 == 0 or quadraticFormulaMinus % 2 == 0:
    print(
        f"The roots can be simplified once or more than once, {qfp2}, {qfm2}")

# if qfp2 % 2 and qfm2 % 2 == 0:
#     print(f"The roots can be simplified again, {qfp22}, {qfm22}.")
