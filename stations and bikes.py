import datetime

import sessions

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

class Station:
    def __init__(self):
        self.bikes = []
        self.balance = 0

    def take_bike(self, bike_id, user):
        bike = [b for b in self.bikes if b["id"] == bike_id]

        if not bike:
            return False

        bike = bike[0]

        if not bike.can_take():
            return False

        if user.get_balance() <= 0:
            return False

        # remove bike from the list
        self.bikes = [b for b in self.bikes if b.id != bike_id]

        return sessions.Session(bike, user, datetime.datetime.now())

class Network:
    def __init__(self, stations):
        self.stations = stations # list

    def get_balance(self):
        return sum([s.balance for s in self.stations])