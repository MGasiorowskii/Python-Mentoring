import time


def timethis(func):
    def inner(t1: float):
        t2 = time.time()
        func(t2 - t1)
    return inner


@timethis
def decorating_time(tim: float):
    print(f"Decorating time: {tim}")


decorating_time(time.time())
