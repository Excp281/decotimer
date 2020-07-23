from timer.every import Every
from timer.keys import keys


def every(key, args=[],
          kwargs={}, milliseconds=0,
          seconds=0, minutes=0,
          hours=0, days=0):
    def decorator(func):
        Every(key, milliseconds,
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


def tick():
    for key in keys.lst:
        keys.lst[key].run()


__all__ = ["tick", "every", "start", "stop", "total", "get"]
