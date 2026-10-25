'''
Strategy Pattern Implementation

use when you want to define a family of algorithms, encapsulate each one, 
and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
Usecase: Applying different discount strategies to a product using a strategy pattern.
'''

from diwali import DiwaliDiscountStrategy
from first_discount import FirstDiscountStrategy
from discount_service import DiscountService

diwali_discount_strategy = DiwaliDiscountStrategy()
first_discount_strategy = FirstDiscountStrategy()
discount_service = DiscountService(first_discount_strategy)

discount_service.process_discount(100)
discount_service.set_discount_strategy(diwali_discount_strategy)
discount_service.process_discount(100)


