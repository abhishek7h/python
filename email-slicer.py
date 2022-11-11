email = input("Enter your email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain}.")