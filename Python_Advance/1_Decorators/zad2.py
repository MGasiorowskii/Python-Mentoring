def add_stairs(func):
    def inner(*args):
        print("*" * 10)
        func(*args)
        print("*" * 10)

    return inner


@add_stairs
def print_txt(*args: str) -> None:
    print(args[0])


print_txt("Hello world!")
