class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
