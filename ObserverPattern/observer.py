from abc import ABC, abstractmethod
import random

class IObservable(ABC):
    """
    Observable interface
    """
    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self, observer):
        pass

class IObserver(ABC):
    """
    Observer Interface
    """
    @abstractmethod
    def update(self):
        pass

class WeatherStation(IObservable):
    """
    Concrete observable
    """

    observers = []
    temperature = None

    def add(self, observer):
        assert isinstance(observer, IObserver)
        self.observers.append(observer)

    def remove(self, observer):
        assert isinstance(observer, IObserver)
        self.observers.remove(observer)

    def notify(self):
        self.set_temperature()
        for observer in self.observers:
            observer.update()

    def get_temperature(self):
        return self.temperature

    def set_temperature(self):
        self.temperature = random.randint(0, 50)


class Phone(IObserver):
    """
    Phone observer, concrete
    """
    def __init__(self, station):
        self.station = station

    def update(self):
        station = self.station
        print('Updating Phone Class')
        print(f'{station.__class__.__name__} {str(station.get_temperature())} °C')
        print()

class LCDDisplay(IObserver):
    """
    Phone observer, concrete
    """
    def __init__(self, station):
        self.station = station

    def update(self):
        station = self.station
        print('Updating LCD Class')
        print(f'{station.__class__.__name__} {str(station.get_temperature())} °C')
        print()


station = WeatherStation()
phone = Phone(station)
lcd_display = LCDDisplay(station)

station.add(phone)
station.add(lcd_display)

station.notify()