class IngegerField:
    def __init__(self, num):
        self.__number = num

    def __get__(self, instance, owner):
        return instance.__dict__[self.__number]

    def __set__(self, instance, value):
        instance.__dict__[self.__number] = value


class Data:
    number = IngegerField("num")

    def __init__(self, num):
        self.number = num


data_row = Data(5)
new_data_row = Data(10)

assert data_row.number != new_data_row.number
