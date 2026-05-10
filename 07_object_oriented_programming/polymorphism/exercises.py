"""
EXERCISES: The Polymorphic Payment System

EXERCISE 1: Payment Interface
1. Create an abstract base class 'PaymentMethod' with an abstract method 'process_payment(amount)'.
2. Create a subclass 'CreditCard' that prints "Processing credit card payment of $[amount]".
3. Create a subclass 'PayPal' that prints "Processing PayPal payment of $[amount]".
4. Create a function 'checkout(payment_obj, amount)' that calls the 'process_payment' method.

EXERCISE 2: The Duck Test
1. Create a class 'Bird' with a method 'fly()'.
2. Create a class 'Airplane' with a method 'fly()'.
3. Write a function 'take_off(entity)' that calls entity.fly().
4. Test it with both a Bird and an Airplane. Note that they don't share a parent class, but they both "fly"!
"""

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

def checkout(payment_obj, amount):
    payment_obj.process_payment(amount)

# ================= 2 ==============

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def take_off(entity):
    entity.fly()

# TODO: Implement the exercises below
if __name__ == "__main__":
    credit_card = CreditCard()
    paypal = PayPal()
    checkout(credit_card, 100)
    checkout(paypal, 200)

    bird = Bird()
    airplane = Airplane()
    take_off(bird)
    take_off(airplane)
