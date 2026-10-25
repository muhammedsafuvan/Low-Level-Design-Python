
from strategy import DiscountStrategy


class DiwaliDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        print(f"Diwali Discount: {price * 0.7}")  # Apply a 30% discount