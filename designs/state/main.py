'''
State Pattern Implementation
use when you want to allow an object to alter its behavior when its internal state changes.
Usecase: Implementing a transport service that can switch between different modes of transportation (Car, Bike, Walking) using a state pattern.
'''

from abc import ABC, abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def directions(self):
        pass

    @abstractmethod
    def eta(self, distance: float) -> float:
        pass


class Car(TransportMode):
    def directions(self):
        return "Driving directions"

    def eta(self, distance: float) -> float:
        return distance / 60


class Bike(TransportMode):
    def directions(self):
        return "Biking directions"

    def eta(self, distance: float) -> float:
        return distance / 15

class Walking(TransportMode):
    def directions(self):
        return "Walking directions"

    def eta(self, distance: float) -> float:
        return distance / 5


class TransportService:
    def __init__(self, transport_mode: TransportMode):
        self.transport_mode = transport_mode

    def get_directions(self):
        return self.transport_mode.directions()

    def get_eta(self, distance: float) -> float:
        return self.transport_mode.eta(distance)

    def set_transport_mode(self, transport_mode: TransportMode):
        self.transport_mode = transport_mode


transport_service = TransportService(Car())
print(transport_service.get_directions())
print(f"ETA for 120 km: {transport_service.get_eta(120)} hours")
transport_service.set_transport_mode(Bike())
print(transport_service.get_directions())
print(f"ETA for 120 km: {transport_service.get_eta(120)} hours")