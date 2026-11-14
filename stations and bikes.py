class Bike:
    def __init__(self, id):
        self.id = id

class ElectricBike(Bike):
    def __init__(self, id):
        super().__init__(id)
        self.price = 5


class RegularBike(Bike):
    def __init__(self, id):
        super().__init__(id)
        self.price = 2

class Station:
    def __init__(self):
        self.bikes = []
        self.balance = 0