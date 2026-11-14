import datetime

import sessions

class Station:
    def __init__(self):
        self.bikes = []
        self.balance = 0

    def take_bike(self, bike_id, user):
        bike = [b for b in self.bikes if b["id"] == bike_id]

        if not user.Session:
            return False

        if not bike:
            return False

        bike = bike[0]

        if not bike.can_take():
            return False

        if user.get_balance() <= 0:
            return False

        # remove bike from the list
        self.bikes = [b for b in self.bikes if b.id != bike_id]

        user.session = sessions.Session(bike, user, datetime.datetime.now())

        return True

    def return_bike(self, user, station):
        if not user.session:
            return False

        bike = user.session.bike
        cost = user.session.cost()

        if not user.minus_money(cost):
            return False

        station.bikes.append(bike)

        user.session = None

        return True

class Network:
    def __init__(self, stations):
        self.stations = stations # list

    def get_balance(self):
        return sum([s.balance for s in self.stations])