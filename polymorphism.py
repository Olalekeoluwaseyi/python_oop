class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling down the street 🚴")

# List of different vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Demonstrating polymorphism
for v in vehicles:
    v.move()
