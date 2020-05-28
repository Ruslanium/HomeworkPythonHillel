def read_file(file="input.txt"):
    """Function to read the file"""
    res = []
    with open(file, encoding='utf-8') as f:
        for i in f.readlines():
            res.append(i.split())
    return res


def write_to_file(line, file="output.txt"):
    """Function to write to file"""
    with open(file, 'w', encoding='utf-8') as f:
        for i in line:
            f.write(' '.join(i) + '\n')


def create_dict(lines):
    """Function to create a dictionary"""
    dict_line = dict()  # dict {line: number of words to delete}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if 3 < len(lines[i][j]) <= 5:
                if i not in dict_line:
                    dict_line[i] = 0
                dict_line[i] += 1
    return dict_line


def delete_word(file="input.txt"):
    """Word delete function"""
    lines = read_file(file)
    dict_line = create_dict(lines)
    for key, value in dict_line.items():
        i = 0
        counter = 0
        if value % 2 != 0:
            value -= 1
        while counter < value:
            if 3 < len(lines[key][i]) <= 5:
                lines[key].pop(i)
                counter += 1
                i -= 1
            i += 1
    write_to_file(lines)


delete_word()
