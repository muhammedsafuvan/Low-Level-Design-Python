'''
Builder Pattern Implementation

use when you want to create complex objects step by step and the construction process 
should allow different representations of the object that is constructed.

Usecase: Building a Laptop object with various specifications using a builder pattern.
'''

class Laptop:
    name:str = None
    ram:str = None
    storage:str = None
    color:str = None
    processessor:str = None

    def display_specs(self):
        if self.name:
            print(f"Laptop Name: {self.name}")
        if self.ram:
            print(f"RAM: {self.ram}")
        if self.storage:
            print(f"Storage: {self.storage}")
        if self.color:
            print(f"Color: {self.color}")
        if self.processessor:
            print(f"Processor: {self.processessor}")


class LaptopBuilder:
    def __init__(self):
        self.laptop = Laptop()

    def set_name(self, name: str):
        self.laptop.name = name
        return self

    def set_ram(self, ram: str):
        self.laptop.ram = ram
        return self

    def set_storage(self, storage: str):
        self.laptop.storage = storage
        return self

    def set_color(self, color: str):
        self.laptop.color = color
        return self

    def set_processor(self, processor: str):
        self.laptop.processessor = processor
        return self

    def build(self) -> Laptop:
        return self.laptop

l1 = LaptopBuilder().set_name("Dell").set_ram("16GB").set_storage("1TB").set_processor("Intel i7").build()
l1.display_specs()

l2 = LaptopBuilder().set_name("HP").set_ram("8GB").set_storage("512GB").set_color("Silver").build()
l2.display_specs()

