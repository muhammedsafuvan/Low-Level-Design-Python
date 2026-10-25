
from strategy import DiscountStrategy


class FirstDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        print(f"First Discount: {price * 0.9}")  # Apply a 10% discount