'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('little fat', 8)
my_dog.sit()
my_dog.roll_over()
'''

class Car(object):
    """模似汽车的类"""
    def __init__(self, make, model, year):
        """汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 95
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name.title())

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles no it.")
    
    def update_odometer(self, mileage):
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        if miles < 0:
            print("Can't increment negative odometer")
        else:
            self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

my_tesla = ElectricCar('tesla', 'model s', '2018')
my_tesla.get_descriptive_name()
my_tesla.describe_battery()

import pizza as pz
pz.make_pizza(25,'extra cheese', 'pepperoni')