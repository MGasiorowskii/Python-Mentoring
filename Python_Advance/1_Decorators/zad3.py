def arg_check(arg):
    def check(old_func):
        def new_func(*args):

            if isinstance(*args, arg):
                print("Types are the same")
            else:
                print("Incorrect type of variable")
        # do sth with arg and call old_func as examp

        return new_func

    return check


@arg_check(str)
def examp(num: int) -> None:
    num += 1


examp(5)
