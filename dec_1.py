def division_ramainder(func):
    def wrapper(*args):
        res = func(*args)
        if res % 100 == 0:
            return "We are OK"
        else:
            return "Bad news guys, we got {}".format(res)
    return wrapper


@division_ramainder
def power(a, b):
    return a**b

print(power(10, 2))
print(power(2, 2))
