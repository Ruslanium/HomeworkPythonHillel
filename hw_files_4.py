def read_file(file="input4.txt"):
    """Функция для считывания файла"""
    res = []
    with open(file, encoding='utf-8') as f:
        for i in f.readlines():
            res.append(i.split())
    for i in res:
        t = i.pop(1).split(':')
        i.insert(1, t[0])
    return res


def create_dict(info):
    """Функция для создания словаря"""
    """
    dict = {ip: {counter:*}, {дни недели: []}, {hours: []}}
    """
    dict_info = dict()
    for i in info:
        ip = i[0]
        hours = i[1]
        weekdays = i[2]
        if ip not in dict_info:
            dict_info[ip] = {}
            dict_info[ip]['counter'] = 0
            dict_info[ip]['hours'] = []
            dict_info[ip]['weekdays'] = []
        dict_info[ip]['counter'] += 1
        dict_info[ip]['hours'].append(hours)
        dict_info[ip]['weekdays'].append(weekdays)
    return dict_info


def write_to_file(info, mode='w', file="output4.txt"):
    """Функция для записи в  файл"""
    with open(file, mode, encoding='utf-8') as f:
        for line in info:
            f.write(' '.join(map(str, line)) + '\n')


def result_info(file="input4.txt"):
    """Функция для создания результирующего массива"""
    dict_info = create_dict(read_file())
    result = []
    dict_of_hours = dict()
    for ip, info in dict_info.items():  # прохожусь по словарю с информацией
        for i in info['hours']:  # считаю для каждого часа кол-во посещений
            if i not in dict_of_hours:
                dict_of_hours[i] = 0
            dict_of_hours[i] += 1
        most_frequent_day = 0  # счетчик для самого частого для для каждого ip
        most_frequent_word = info['weekdays'][0]
        for i in info['weekdays']:
            if most_frequent_day < info['weekdays'].count(i):
                most_frequent_day = info['weekdays'].count(i)
                most_frequent_word = i
        result.append([ip, info['counter'], most_frequent_word])

    max_number = 0
    most_frequent_hour = 0
    for hour, number in dict_of_hours.items():  # прохожусь по словарю с часами, чтобы найти самый популярный
        if number > max_number:
            max_number = number
            most_frequent_hour = hour
    result.append(['Самый популярный час на сайте:', most_frequent_hour])
    write_to_file(result)


result_info()
