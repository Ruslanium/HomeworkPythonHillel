def read_file(file="input2.txt"):
    """Функция для считывания файла"""
    res = []
    with open(file, encoding='utf-8') as f:
        for i in f.readlines():
            res.append(i.split())
    return res


def create_dict(lines):
    """Функция для создания словаря"""
    name_phones = dict()  # словарь {фамилия: [телефоны]}
    for i in lines:
        if i[0] not in name_phones:
            name_phones[i[0]] = [i[1]]
        else:
            name_phones[i[0]].append(i[1])
    return name_phones


def write_to_file(record='', mode='a', file="output2.txt"):
    """Функция для записи в  файл"""
    with open(file, mode, encoding='utf-8') as f:
        f.write(record)


def surname_verification(file="input2.txt"):
    result = read_file()
    name_phones = create_dict(result)
    for name, phones in name_phones.items():
        if name.startswith('К') or name.startswith('С'):  # проверка на первую букву фамилии
            record = "{0} {1}{2}".format(name, ' '.join(phones), '\n')
            write_to_file(record)


write_to_file(mode='w')
surname_verification()
