# Create a function that checks whether a password:

# Has at least 8 characters
# Contains uppercase
# Contains lowercase
# Contains digit
# Contains special character

def check_password(password):
    return {
        "length": len(password) >= 8,
        "uppercase": any(ch.isupper() for ch in password),
        "lowercase": any(ch.islower() for ch in password),
        "digit": any(ch.isdigit() for ch in password),
        "special_char": any(not ch.isalnum() for ch in password)
    }


password = input("Enter your password: ")
result = check_password(password)

print(result)
