
from typing import List

from observer import Observer


class WeatherStation:
    def __init__(self):
        self.__observers: List[Observer] = []
        self.temperature : float = 0.0

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def set_temperature(self, temp: float):
        self.temperature = temp
        self.notify_observers()

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.temperature)