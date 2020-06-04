class Ip:
    def __init__(self, li):
        self.list_ip = li

    def __str__(self):
        return "\n".join(self.list_ip)

    def reverse_ip(self):
        revers_ip = []
        for ip in self.list_ip:
            octets = ip.split('.')
            revers_ip.append('.'.join([octets[3], octets[2], octets[1], octets[0]]))
        return Ip(revers_ip)

    def without_first_octets(self):
        result_ip = []
        for ip in self.list_ip:
            octets = ip.split('.')
            result_ip.append('.'.join([octets[1], octets[2], octets[3]]))
        return Ip(result_ip)

    def last_octets(self):
        result = []
        for ip in self.list_ip:
            octets = ip.split('.')
            result.append(str(octets[3]))
        return Ip(result)


list_ip = ['10.11.12.13', '10.14.15.13', '9.14.11.13', '18.11.17.13',
           '11.15.12.14', '13.7.16.13', '13.9.12.15', '11.15.11.13']

a = Ip(list_ip)
print(a, '\n')
print(a.without_first_octets(), '\n')
print(a.reverse_ip(), '\n')
print(a.last_octets(), '\n')
