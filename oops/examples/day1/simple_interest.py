class Interest:
    def get_amount(self):
        self.principal = float(input("Enter the principal:"))
        self.rate = float(input("Enter rate of interest:"))
        self.time = float(input("Enter time(years):"))

    def put_amount(self):
        int_amt = (self.principal*self.rate*self.time)/100
        total_amt = int_amt + self.principal
        print("The interest is : ",int_amt)
        print("The total amount is : ",total_amt)


interest = Interest()
interest.get_amount()
interest.put_amount()