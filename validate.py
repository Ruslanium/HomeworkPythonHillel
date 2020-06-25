class EmailDescriptor:
    def __init__(self, email):
        self.__email = email

    def __get__(self, instance, owner):
        return instance.__dict__[self.__email]

    def __set__(self, instance, value):
        valid_email = ['gmail.com', 'ukr.net', 'mail.ru']
        if '@' not in value or value.find('@') == len(value) - 1:
            raise ValueError("Error")
        elif value.split('@')[1] not in valid_email:
            raise ValueError("Некорректный ввод")
        else:
            print("Success")
            instance.__dict__[self.__email] = value


class MyClass:
    email = EmailDescriptor("email")

    def __init__(self, e):
        self.email = e


my_class = MyClass("validemail@gmail.com")
my_class.email = "novalidemail@ukr.net"

