from datetime import datetime


class Timer:
    def __init__(self):
        self.start = datetime.now()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now() - self.start)


def power(a, b):
    return a**b


with Timer() as t:
    print(power(2, 1000000))

