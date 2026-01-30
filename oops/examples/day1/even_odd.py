class Number:
    def get_num(self):
        self.num = int(input("Enter a number:"))
    def put_num(self):
        if self.num % 2 == 0:
            print("Given number is an Even number")
        else:
            print("Given number is an Odd number")

number = Number()
number.get_num()
number.put_num()