'''
Facade Pattern Implementation
use when you want to provide a simplified interface to a complex subsystem.
Usecase: Providing a simplified interface to access user and order services using a facade pattern.'''
class UserService:
    def get_user(self, user_id: str) -> str:
        return f"User details for user_id: {user_id}, name: John Doe"

    def login(self, username: str, password: str) -> bool:
        print(f"Logging in user: {username}")
        return True


class OrderService:
    def get_order_details(self, order_id: str) -> str:
        print(f"Fetching order details for order_id: {order_id}")
        return f"Order details for order_id: {order_id}, item: Laptop, quantity: 1"



class APIServiceFacade:
    def __init__(self):
        self.user_service = UserService()
        self.order_service = OrderService()

    def get_user_info(self, user_id: str) -> str:
        return self.user_service.get_user(user_id)

    def login_user(self, username: str, password: str) -> bool:
        return self.user_service.login(username, password)

    def get_order_info(self, order_id: str) -> str:
        return self.order_service.get_order_details(order_id)

    def get_all_info(self, user_id: str, order_id: str) -> str:
        user_info = self.login_user("john_doe", "password123")  # Example
        user_info = self.get_user_info(user_id)
        order_info = self.get_order_info(order_id)
        return f"{user_info}\n{order_info}"


user_id = "12345"
order_id = "98765"
api_facade = APIServiceFacade()

print(api_facade.get_all_info(user_id, order_id))
