from functools import wraps


def type_of_argument(func):
    @wraps(func)

    def wrapper(*args):
        if isinstance(*args, int):
            return func(*args)
        elif isinstance(*args, str):
            raise ValueError("string type is not supported")
        else:
            return 0
    return wrapper


@type_of_argument
def my_func(a):
    return a**2


print(my_func(2))
print(my_func('str'))