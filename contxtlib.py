import os
from contextlib import ContextDecorator


class ChangeDir(ContextDecorator):
    def __init__(self, path, *exception):
        self.path = path
        self.exception = exception
        self.w_dir = os.getcwd()

    def __enter__(self):
        try:
            os.chdir(self.path)
        except self.exception as e:
            print("Error: ", e)
        except Exception:
            pass

    def __exit__(self, exc_tp, exc_val, exc_tb):
        os.chdir(self.w_dir)


@ChangeDir('test', FileNotFoundError)
def func():
    print(os.getcwd())


func()