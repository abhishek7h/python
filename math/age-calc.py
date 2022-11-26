bday = int(input('In which year were you born? '))

age = 2022 - bday

print(f'You are {age} years old.')

if age >= 18:
    print(f'PS: Since you are {age} years old, you are legally an adult. ')
else:
    print(f'PS: You are legally not an adult, since you are {age}.')
