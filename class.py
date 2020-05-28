# class Group:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return str(self.name)


class Students:
    __slots__ = "second_name", "initials", "group", "progress"

    def __init__(self, second_name='Some name', initials='some init', group=3, **kwargs):
        self.second_name = second_name
        self.initials = initials
        self.group = group
        self.progress = kwargs

    def __str__(self):
        result = "{} {}, {}, {}".format(self.second_name, self.initials, self.group, self.progress)
        return result

    def __get__(self):
        return [self.second_name, self.initials, self.group, self.progress]


class UserInfoAggregator:

    def __init__(self, data):
        self.result = []
        for item in data:
            for key, value in item.items():
                name, init, group, prog = key[0], key[1], value[0], value[1]
                self.result.append(Students(name, init, group, **prog))

    """У меня не получилось сделать, используя класс Group. Как правильно обратиться к нему?"""
    def excellent_students(self):
        brain = []
        for students in self.result:
            name, init, group, subject_dict = students.second_name, \
                                              students.initials, students.group, students.progress
            clever = True
            for subject, mark in subject_dict.items():
                if mark < 4:
                    clever = False
            if clever:
                brain.append([name, init, group])
        return brain


data = [{('Иванов', 'А.А.'): [1, {'мат': 4, 'фил': 5}]},
        {('Петров', 'А.В.'): [3, {'лит': 5, 'ист': 3}]},
        {('Сидоров', 'А.Г.'): [2, {'физ': 4, 'лит': 5}]},
        {('Краснов', 'М.М.'): [4, {'фил': 5, 'ист': 4}]},
        {('Кузнецов', 'К.К.'): [3, {'мат': 4, 'черч': 3}]},
        {('Шевченко', 'В.Б.'): [5, {'черч': 3, 'фил': 5}]}]

gruppa1 = UserInfoAggregator(data)
print(gruppa1.excellent_students())
