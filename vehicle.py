class Vehicle:
    def __init__ (self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
        self._engine_started = False

    def start_engine (self):
        self._engine_started = True
        print(f"{self.brand} {self.model}'s engine is running")

    def stop_engine(self):
        self._engine_started = False
        print(f"{self.brand} {self.model}'s engine stopped")

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"
    

class EletricCar(Vehicle):
    def __init__(self, brand, year, model, battery_capacity):
        super().__init__(brand, year, model)
        self.baterry_capacity = battery_capacity
        self.charge_level = 100

    def start_engine(self):
        if self.charge_level > 0:
            self._engine_started = True
            print(f"{self.get_info()} (Electric) started with {self.charge_level}% baterry.")

        else:
            print(f"{self.get_info()} can not start. Battery is Low")

    def charge(self, amount):
        self.charge_level = min(100, self.charge_level + amount)
        print(f"{self.get_info()} charged to {self.charge_level}%.")

    def stop_engine(self):
        self._engine_started = False
        print(f"{self.brand} {self.model}'s engine stopped.")

benz = Vehicle(brand = "Mercedes-Benz", year = 2024, model = "G-Wagon")
print(benz.get_info())
benz.start_engine()
print(benz._engine_started)
benz.stop_engine()

tesla = EletricCar(brand = "Tesla", year = 2025, model = "Cybertruck", battery_capacity=100)
tesla.start_engine()
tesla.charge(-90)
tesla.stop_engine()

