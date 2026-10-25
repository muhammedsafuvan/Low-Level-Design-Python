
'''
Decorator Pattern Implementation
use when you want to add new functionality to an existing object without altering its structure.
Usecase: Adding milk, sugar, and whipped cream to a coffee object using a decorator pattern'''

from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def prepare(self):
        pass
    @abstractmethod
    def cost(self)->float:
        pass

class Coffee(Beverage):
    def prepare(self):
        return "Preparing coffee"

    def cost(self) -> float:
        return 20

class AddOnDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def prepare(self):
        pass

    
    def cost(self) -> float:
        pass


class Milk(AddOnDecorator):
    def prepare(self):
        return self.beverage.prepare() + ", milk"

    def cost(self) -> float:
        return self.beverage.cost() + 10


class Sugar(AddOnDecorator):
    def prepare(self):
        return self.beverage.prepare() + ", sugar"

    def cost(self) -> float:
        return self.beverage.cost() + 5

class WhippedCream(AddOnDecorator):
    def prepare(self):
        return self.beverage.prepare() + ", whipped cream"

    def cost(self) -> float:
        return self.beverage.cost() + 15


coffee = Coffee()
print(f"Coffee preparation: {coffee.prepare()}")
print(f"Total cost: {coffee.cost()}")
coffee = Milk(coffee)
print(f"Coffee preparation: {coffee.prepare()}")
print(f"Total cost: {coffee.cost()}")
coffee = Sugar(coffee)
print(f"Coffee preparation: {coffee.prepare()}")
print(f"Total cost: {coffee.cost()}")
coffee = WhippedCream(coffee)

print(f"Coffee preparation: {coffee.prepare()}")
print(f"Total cost: {coffee.cost()}")
