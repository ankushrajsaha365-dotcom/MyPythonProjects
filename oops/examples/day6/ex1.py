from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")


class UPI(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")


payments = [CreditCard(), UPI()]

for method in payments:
    method.pay(1000)
