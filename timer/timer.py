from time import time


WORKING = 0
STOPPED = 1


class Keys:
    def __init__(self):
        self.lst = {}

    def set(self, key, value):
        if key in self.lst.keys():
            raise ValueError("Duplicate key: %s" % key)
        else:
            self.lst.update({key: value})

    def get(self, key):
        if key not in self.lst.keys():
            raise ValueError("Key not found: %s" % key)
        else:
            return self.lst[key]


class Schedule:
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
            + self.days * 24*3600
        self.last_tick = time()

        self.total = 0

    def start(self):
        self.status = WORKING

    def stop(self):
        self.status = STOPPED

    def run(self):
        if self.status == WORKING:
            if time() - self.last_tick >= self.tick_time:
                self.func(*self.args, **self.kwargs)
                self.last_tick = time()
                self.total += 1


def schedule(key, args=[],
             kwargs={}, milliseconds=0,
             seconds=0, minutes=0,
             hours=0, days=0,):
    if args is None:
        args = []

    def decorator(func):
        Schedule(key, milliseconds,
                 seconds, minutes,
                 hours, days,
                 func, *args,
                 **kwargs)
        return func

    return decorator


def start(key):
    keys.get(key).start()


def stop(key):
    keys.get(key).stop()


def total(key):
    return keys.get(key).total


def get(key):
    return keys.get(key)


keys = Keys()


def tick():
    for key in keys.lst:
        keys.lst[key].run()


__all__ = ["tick", "schedule", "start", "stop", "total", "get"]
