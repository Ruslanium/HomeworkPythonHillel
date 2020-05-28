def read_file(file="input4.txt"):
    """Function to read the file"""
    res = []
    with open(file, encoding='utf-8') as f:
        for i in f.readlines():
            res.append(i.split())
    for i in res:
        t = i.pop(1).split(':')
        i.insert(1, t[0])
    return res


def create_dict(info):
    """Function to create a dict"""
    """
    dict = {ip: {counter:*}, {weekdays: []}, {hours: []}}
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
    """Function to write to file"""
    with open(file, mode, encoding='utf-8') as f:
        for line in info:
            f.write(' '.join(map(str, line)) + '\n')


def result_info(file="input4.txt"):
    """Function to create the resulting list"""
    dict_info = create_dict(read_file())
    result = []
    dict_of_hours = dict()
    for ip, info in dict_info.items():  # I go through the dictionary with information
        for i in info['hours']:  # I consider for each hour the number of visits
            if i not in dict_of_hours:
                dict_of_hours[i] = 0
            dict_of_hours[i] += 1
        most_frequent_day = 0  # counter for the most frequent for for each ip
        most_frequent_word = info['weekdays'][0]
        for i in info['weekdays']:
            if most_frequent_day < info['weekdays'].count(i):
                most_frequent_day = info['weekdays'].count(i)
                most_frequent_word = i
        result.append([ip, info['counter'], most_frequent_word])

    max_number = 0
    most_frequent_hour = 0
    for hour, number in dict_of_hours.items():  # I go through the dict with the hours to find the most popular
        if number > max_number:
            max_number = number
            most_frequent_hour = hour
    result.append(['Самый популярный час на сайте:', most_frequent_hour])
    write_to_file(result)


result_info()
