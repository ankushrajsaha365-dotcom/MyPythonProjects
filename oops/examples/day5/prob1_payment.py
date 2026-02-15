# Payment system

class Payment:
    def pay(self):
        print("Payment method not available!!!")

class CreditCard(Payment):
    def pay(self):
        print("Processing...")

class PayPal(Payment):
    def pay(self):
        print("Redirecting...")

class UPI(Payment):
    def pay(self):
        print("Scaning QR code...")

creditcard = CreditCard()
paypal = PayPal()
upi = UPI()

methods  = [creditcard , paypal , upi]

for method in methods:
    method.pay()

