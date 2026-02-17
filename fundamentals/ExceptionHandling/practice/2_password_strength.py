# Ask user to enter a password.

# Rules:

# Minimum length = 8
# Must contain at least one digit
# Must contain at least one uppercase letter
# Raise custom exceptions:
# WeakPasswordError

class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter password:")

    if len(password) < 8:
        raise WeakPasswordError("Password length should be atleast 8")
    
    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain at least one digit")
    
    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Password must contain at least one uppercase letter")

except WeakPasswordError as e:
    print(e)

else:
    print("Password verified...")