def read_file(file="input3.txt"):
    """Функция для считывания файла"""
    res = []
    with open(file, encoding='utf-8') as f:
        for i in f.readlines():
            res.append(i.strip())
    return res


def max_len(arr):
    """Считаем максимальную длину строки в файле"""
    len_max = 0
    for i in arr:
        len_max = max(len_max, len(i))
    return len_max


def write_to_file(arr, mode='w', file="output3.txt"):
    """Функция для записи в  файл"""
    with open(file, mode, encoding='utf-8') as f:
        for i in arr:
            f.write(i)
            f.write('\n')


def alignment(file="input3.txt"):
    """Выравниваем по правому краю"""
    li = read_file(file)
    lines_max_len = max_len(li)
    res = []
    for i in li:
        res.append(i.rjust(lines_max_len, ' '))
    write_to_file(res)


alignment()
