from observer import Observer


class TVObserver(Observer):
    def update(self, temp: float):
        print(f"TV Observer: Temperature updated to {temp}°C")