from datetime import time, datetime, timedelta


class Session:
    def __init__(self, bike, user, time_start):
        self.bike = bike
        self.user = user
        self.time_start = time_start

    def cost(self):
        now = datetime.now()
        diff = now - self.time_start
        duration = diff.minute
        return self.bike.cost(duration)










