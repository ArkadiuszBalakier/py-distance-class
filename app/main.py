from __future__ import annotations
from typing import Union

class Distance:
    def __init__(self, km : int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance , int , float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: Union[Distance , int , float]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        return NotImplemented


    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            distance = Distance(self.km * other)
            return distance
        return NotImplemented

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            else:
                distance = Distance(round(self.km / other, 2))
                return distance
        return NotImplemented

    def __lt__(self, other: Union[Distance , int , float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km

        return NotImplemented

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km

        return NotImplemented

    def __eq__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km

        return NotImplemented

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km

        return NotImplemented

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km

        return NotImplemented
