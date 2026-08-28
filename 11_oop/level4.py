class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")
    
sounds = [Dog(),Cat()]
for sound in sounds:
    sound.speak()
    
class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Beep")
        
def make_speak(obj):
    obj.speak()
    
make_speak(Dog())
make_speak(Robot())

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
class  Dog(Animal):
    def speak(self):
        pass
class Cat(Animal):

    def speak(self):
        print("Meow")
        
        
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
class StripePayment(Payment):

    def pay(self, amount):
        print(f"Stripe payment: {amount}")
class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"PayPal payment: {amount}")
class BankPayment(Payment):

    def pay(self, amount):
        print(f"Bank payment: {amount}")
        
        
payments = [
    StripePayment(),
    PayPalPayment(),
    BankPayment()
]

for payment in payments:
    payment.pay(1000)