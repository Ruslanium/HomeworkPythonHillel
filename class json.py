import json
import os


class Json:
    def __init__(self, path):
        with open(path, 'r') as f:
            self.info_dict = json.load(f)

    def write_to_file(self, path):
        with open(path, 'w') as f:
            json.dump(self.info_dict, f)

    def union_data_and_write_to_file(self, union, output):
        """joins union list data by key and writes in output"""
        for file in union:
            with open(file, 'r') as f:
                res = json.load(f)
                for key, value in res.items():
                    if key not in self.info_dict:
                        self.info_dict[key] = []
                    self.info_dict[key].append(value)
        self.write_to_file(output)

    def absolute_path(self, name):
        return os.path.abspath(name)

    def relative_path(self, path):
        return os.path.relpath(path)


a = Json(r"F:\Programming\Python\Python study\Hillel\Practice\hw_7\info.json")
a.write_to_file('output.json')
a.union_data_and_write_to_file(["info2.json", "info3.json"], "result.json")
print(a.absolute_path("test.json"))
print(a.relative_path(r"F:\Programming\Python\Python study\Hillel\Practice\hw_7\test\test2\test.json"))

