from decotimer.repeat import Repeat
from decotimer.wait import Wait
from decotimer.keys import keys
from copy import copy


def repeat(key, autoenable=True, milliseconds=0,
           seconds=0, minutes=0,
           hours=0, days=0,
           args=[], kwargs={}, ):
    def decorator(func):
        Repeat(key, autoenable, milliseconds,
               seconds, minutes,
               hours, days,
               func, *args,
               **kwargs)
        return func

    return decorator


def wait(key, autoenable=True, milliseconds=0,
         seconds=0, minutes=0,
         hours=0, days=0,
         args=[], kwargs={}, ):
    def decorator(func):
        Wait(key, autoenable, milliseconds,
             seconds, minutes,
             hours, days,
             func, *args,
             **kwargs)
        return func

    return decorator


def enable(key):
    keys.get(key).enable()


def disable(key):
    keys.get(key).disable()


def total(key):
    return keys.get(key).get_total()


def get(key):
    return keys.get(key)


def tick():
    lst = copy(keys.lst)
    for key in lst:
        keys.lst[key].run()


__all__ = ["tick", "repeat", "wait", "enable", "disable", "total", "get"]
