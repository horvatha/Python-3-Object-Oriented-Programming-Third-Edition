"""
Before using flyweight to optimize memory usage try slots
See: https://realpython.com/python-data-classes/
"""

from dataclasses import dataclass
from timeit import timeit

from pympler import asizeof


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float


simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
size = asizeof.asizesof(simple, slot)

print(size)

print(dir(simple))
print(dir(slot))
print(simple.__dir__())
print(slot.__dir__())
print(simple.__dict__)  # {'name': 'London', 'lon': -0.1, 'lat': 51.5}
# print(slot.__dict__)  # AttributeError


time_simple = timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals())
time_slot = timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals())
print(f"times - simple: {time_simple}, slot: {time_slot}")  # With Py 3.9 there is no much difference,
                                                            # the letter tends to be faster



