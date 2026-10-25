


from strategy import DiscountStrategy


class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def process_discount(self, price: float) -> float:
        return self.discount_strategy.calculate_discount(price)

    def set_discount_strategy(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy