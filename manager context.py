import os


class ChangeDir:
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


with ChangeDir("fgdg", FileNotFoundError):
    print(os.getcwd())
