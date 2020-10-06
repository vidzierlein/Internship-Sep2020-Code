"""Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
"""

class celcius_to_farenheit():
    "Convert temperature in celcius to farenheit"

    def __init__(self, farenheit, celcius):
        self.farenheit= 0
        self.celcius = 0
    
    def convert_celcius_to_farenheit(self):
        farenheit = ((celcius * 9)/5) + 32

    def convert_farenheit_to_celcius(self):
        celcius = ((farenheit - 32) * 5)/9
    
    def display_temp(self):
        self.farenheit = farenheit
        print(farenheit)

    celcius_to_farenheit.object = 


class farenheit_to_celcius():
    pass