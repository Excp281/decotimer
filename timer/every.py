from timer.keys import keys
from timer.constants import WORKING, STOPPED
from time import time


class Every:
    def __init__(self, key, milliseconds,
                 seconds, minutes,
                 hours, days,
                 func, *args, **kwargs):
        keys.set(key, self)
        self.key = key
        self.milliseconds = milliseconds
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.func = func
        self.args = args
        self.kwargs = kwargs

        self.status = STOPPED

        self.tick_time = self.milliseconds / 1000 + self.seconds \
            + self.minutes * 60 + self.hours * 3600 \
            + self.days * 24 * 3600
        self.last_tick = time()

        self.total = 0

    def start(self):
        self.status = WORKING

    def stop(self):
        self.status = STOPPED

    def run(self):
        if self.status == WORKING:
            tick_time = time() - self.last_tick
            if tick_time >= self.tick_time:
                self.last_tick = time() + self.tick_time - tick_time
                self.func(*self.args, **self.kwargs)
                self.total += 1
