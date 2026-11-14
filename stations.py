import datetime

import sessions
from bike import Bike


class Station:
    def __init__(self, bikes):
        self.bikes = bikes
        self.balance = 0

    def take_bike(self, bike_id, user):
        bike = [b for b in self.bikes if b.id == bike_id]

        if user.session:
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

    def return_bike(self, user):
        if not user.session:
            return False

        bike = user.session.bike
        cost = user.session.cost()

        if not user.minus_money(cost):
            return False

        time_passed = user.session.time_passed()
        bike.return_bike(time_passed) # update bike class

        # update station
        self.bikes.append(bike)
        self.balance += cost

        user.session = None

        return True


class Network:
    def __init__(self, stations):
        self.stations = stations # list

    def get_balance(self):
        return round(sum([s.balance for s in self.stations]),2)