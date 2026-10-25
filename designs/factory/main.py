
from factory import FoodFactory
from restuarent import RestuarentService


food_factory = FoodFactory()
restaurent_service = RestuarentService(food_factory)
restaurent_service.prepare_food("burger")
restaurent_service.prepare_food("pizza")