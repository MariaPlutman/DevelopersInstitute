import re
import datetime

# Exercise 1
# Use the regular expression module to extract numbers from a string
'''def ex1(str):
    numbers = re.findall(r'[0-9]+', str)
    return array


str = "5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength."
numbers = ex1(str)
print(*array)'''

# Exercise 2
'''class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        seconds = self.seconds
        answer = seconds/31557600
        return round(answer, 2)

    def on_mercury(self):
        seconds = self.seconds
        answer = seconds/(86400*87.969257175)
        return round(answer, 2)

    def on_venus(self):
        seconds = self.seconds
        answer = seconds/((0.61519726*365.25)*86400)
        return round(answer, 2)

    def on_mars(self):
        seconds = self.seconds
        answer = seconds/((1.8808158*365.25)*86400)
        return round(answer, 2)

    def on_jupiter(self):
        seconds = self.seconds
        answer = seconds/((11.862615*365.25)*86400)
        return round(answer, 2)

    def on_saturn(self):
        seconds = self.seconds
        answer = seconds/((29.447498*365.25)*86400)
        return round(answer, 2)

    def on_uranus(self):
        seconds = self.seconds
        answer = seconds/((84.016846*365.25)*86400)
        return round(answer, 2)

    def on_neptune(self):
        seconds = self.seconds
        answer = seconds/((164.79132*365.25)*86400)
        return round(answer, 2)


space_age = SpaceAge(1000000000)
print(space_age.on_earth())
'''
