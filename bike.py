class Bike:
    def __init__(self, id):
        self.id = id

    def can_take(self):
        return True

class ElectricBike(Bike):
    def __init__(self, id, charged):
        super().__init__(id)
        self.price = 5
        self.charged = charged

    def can_take(self):
        return self.charged

class RegularBike(Bike):
    def __init__(self, id):
        super().__init__(id)
        self.price = 2