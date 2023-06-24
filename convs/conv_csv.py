from convs.abc_conv import ABCConv
import csv


class Csv(ABCConv):

    def convert(self) -> object:
        pass

    def __init__(self):
        _object = None

    def import_file(self, path_to_file, encoding="UTF-8", delimiter=";"):
        obj = dict()
        root = dict()
        with open(path_to_file, encoding=encoding) as csv_raw:
            csv_file = csv.reader(csv_raw, delimiter=delimiter)
            rows = []
            head = csv_file.__next__()
            for row in csv_file:
                rows += [row]
            for i, r in enumerate(rows):
                row_dict = dict()
                for j, d in enumerate(r):
                    row_dict[head[j]] = d
                root[i] = row_dict
            obj["root"] = root
            return obj

    def export_file(self, json_obj, path_to_file, rewrite: bool):
        for c in json_obj:
            for e in c:
                print(e)
                # Todo: export for csv

        return False
