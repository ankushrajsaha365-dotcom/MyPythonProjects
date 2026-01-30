class Compare:
    def get_num(self):
        self.a = int(input("Enter a number a:"))
        self.b = int(input("Enter a number b:"))
        self.c = int(input("Enter a number c:"))

    def put_num(self):
        if self.a == self.b == self.c:
            print("All the numbers are same\nCan't compare them")

        elif self.a >= self.b and self.a >= self.c:
            if self.a == self.b or self.a == self.c:
                print("a shares the largest value")
            else:
                print("a is the largest")

        elif self.b >= self.a and self.b >= self.c:
            if self.b == self.c:
                print("b and c have the same value\nBoth are the largest")
            else:
                print("b is the largest")

        else:
            print("c is the largest")


compare = Compare()
compare.get_num()
compare.put_num()