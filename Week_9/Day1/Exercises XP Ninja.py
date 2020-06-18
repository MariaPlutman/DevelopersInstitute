from abc import ABC, abstractmethod


class Temperature(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def convert(self, to):
        pass


class Celsius(Temperature):
    def convert(self, to):
        """
        to: str
            the temperature format to convert to (can be 'kelvin' or 'fahrenheit')
        """
        if to == 'kelvin':
            return self.value + 273.15
        elif to == 'fahrenheit':
            return 32 + (self.value * 9/5)


class Fahrenheit(Temperature):
    def convert(self, to):
        """
        to: str
            the temperature format to convert to (can be 'kelvin' or 'fahrenheit')
        """
        if to == 'kelvin':
            return Fahrenheit(self.value - 32)*5/9+273.15
        elif to == 'celsius':
            return 32 + (self.value * 9/5)-32


temperature = Celsius(25)
