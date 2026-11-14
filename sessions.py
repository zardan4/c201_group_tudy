from datetime import datetime


class Session:
    def __init__(self, bike, user, time_start):
        self.bike = bike
        self.user = user
        self.time_start = time_start

    def time_passed(self):
        now = datetime.now()
        diff = now - self.time_start
        return diff.total_seconds() / 60

    def cost(self):
        duration = self.time_passed()
        cost = self.bike.price * duration
        return cost










