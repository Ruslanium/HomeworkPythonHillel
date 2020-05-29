class ParameterStorage:
    def __init__(self):
        self._unit_name = None
        self._mac_address = None
        self._ip_address = None
        self._login = None
        self._password = None

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = str(value)

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = str(value)

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = str(value)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = str(value)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = str(value)

    def __str__(self):
        return '\n'.join(map(str, [self._unit_name, self._mac_address, self._ip_address, self._login, self._password]))


connection = ParameterStorage()
connection.login = 'user'
connection.password = 'qwerty'
connection.unit_name = 'PC'
connection.ip_address = 'some ip'
connection.mac_address = 'some mac'
print(connection)
