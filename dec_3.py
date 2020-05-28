from functools import wraps


def cache(func):
    cache = {}
    count_new_call = 0   # переменная для хранения вызовов функции с новыми аргументами
    count_cache_call = 0   # переменная для хранения вызовов функции из кэша

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            nonlocal count_new_call
            count_new_call += 1
            return "Function executed with counter = {}, function result = {}".format(count_new_call, cache[args])
        else:
            nonlocal count_cache_call
            count_cache_call += 1
            return "Used cache with counter = {}".format(count_cache_call)
    return wrapper


@cache
def my_func(a):
    return a**2


print(my_func(2))
print(my_func(2))
print(my_func(2))
print(my_func(3))
print(my_func(4))
print(my_func(4))
print(my_func(4))
print(my_func(3))
print(my_func(3))

