class Calculator:
    def get_value(self):
        self.a = float(input("Enter a number a:"))
        self.b = float(input("Enter a number b:"))
        print("MENU\n 1-> ADD \n 2-> SUB \n 3-> MUL \n 4-> DIV")
        self.op = int(input("Enter operation: "))
    def put_value(self):
        if self.op in range(1,5):
            if self.op == 1:
                print(self.a + self.b)
            elif self.op == 2:
                print(self.a - self.b)
            elif self.op == 3:
                print(self.a * self.b)
            else:
                if self.b != 0:
                    print(self.a / self.b)
                else:
                    print("Divider can't be zero!!!")
        else:
            print("Invalid operation selected")

calculator = Calculator()
calculator.get_value()
calculator.put_value()