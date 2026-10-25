'''
Observer Pattern Implementation
use when you want to define a one-to-many dependency between objects so that when one object changes
 state, all its dependents are notified and updated automatically.
Usecase: Implementing a weather station that notifies multiple display devices (TV, Mobile) when the temperature changes using an observer pattern.
'''
from weather_station import WeatherStation
from mobile import MobileObserver
from tv import TVObserver

weather_station = WeatherStation()
tv_display = TVObserver()
mobile_display = MobileObserver()

weather_station.add_observer(mobile_display)
weather_station.add_observer(tv_display)

weather_station.set_temperature(25.0)
weather_station.remove_observer(mobile_display)
weather_station.set_temperature(30.0)