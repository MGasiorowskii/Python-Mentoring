from typing import Any


def logged(func):
   def inner(*args, **kwargs):
      print(f"you called {func.__name__}{args} it returned {func(*args, **kwargs)}")

   return inner


@logged
def count(*args: list[Any]) -> int:
   return 3 + len(args)


count(4, 4, 4)
