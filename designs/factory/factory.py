
'''
Factory Pattern Implementation
use when you want to create objects without specifying the exact class of object that will be created.
Usecase: Creating different types of food items (Burger, Pizza) using a factory pattern.'''
from burger import Burger
from pizza import Pizza


class FoodFactory:
    def __init__(self):
        self.food_types = {
            "burger": Burger,
            "pizza": Pizza
        }
    
    def create_food(self, food_type: str):
        food_class = self.food_types.get(food_type.lower())
        if food_class:
            return food_class()
        else:
            raise ValueError(f"Unknown food type: {food_type}")