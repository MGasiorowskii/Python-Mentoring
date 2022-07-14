from typing import Any, Union, Optional, Callable
from dataclasses import dataclass

def multiply(factor: int, text: str) -> str:
    """
    Function multiply given text times factor
    """

    return factor * text

x: str = "lorem ipsum"
y: int = 100_000_000
c: float = 3.5
i: bool = True

p: list[int] = [1, 2, 3]

first_tup: tuple[int, ...] = (1, 2, 5, 3, 2 ,1 )

sett: set[int] = {1, 2, 3}

dictt: dict[str, int] = {"str": 5}


l1: list[Union[str, int]] = ["1", 1, 1.5]

def multiply(a: int, b: int, c: Optional[int] = None) -> int:
    return a*b*c if c else a*b

def do_something(): pass


func: Callable = do_something


@dataclass
class Point:
    y: int = 0
    x: int = 0

p: Point = Point()
