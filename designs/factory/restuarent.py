
from factory import FoodFactory


class RestuarentService:
    def __init__(self, food_factory: FoodFactory):
        self.food_factory = food_factory

    def prepare_food(self, food_type: str):
        food = self.food_factory.create_food(food_type)
        food.prepare()