# Login System

# Constructor: username, password
# Method: verify login (hardcoded credentials)


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify(self):
        org_username = "XYZ"
        org_password = "1234"

        if self.username == org_username and self.password == org_password:
            print("Login verified")
        else:
            print("Wrong credentials")


username = input("Enter username: ")
password = input("Enter password: ")

login = Login(username, password)
login.verify()
