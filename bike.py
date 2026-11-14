class Bike:
    def __init__(self, id):
        self.id = id

    def can_take(self):
        return True

    def return_bike(self):
        pass

class ElectricBike(Bike):
    def __init__(self, id, charge):
        super().__init__(id)
        self.price = 5
        self.charge = charge # 0-100

    def can_take(self):
        return self.charge >= 20

    def return_bike(self, time):
        if self.charge < time:
            self.charge = 0

        self.charge -= time

class RegularBike(Bike):
    def __init__(self, id):
        super().__init__(id)
        self.price = 2