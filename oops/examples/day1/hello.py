class Hello:
    def get_details(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))
    
    def check(self):
        if self.age >= 18:
            print(f"Hello {self.name} , you are welcome!!!")
        else:
            print("Sorry you can't enter!!!")

hello = Hello()            
hello.details()
hello.check()