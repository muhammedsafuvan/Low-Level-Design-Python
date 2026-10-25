from observer import Observer


class MobileObserver(Observer):
    def update(self, temp: float):
        print(f"Mobile Observer: Temperature updated to {temp}°C")