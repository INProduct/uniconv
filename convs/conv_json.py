import json
from convs.abc_conv import ABCConv


class Json(ABCConv):

    def import_file(self, path_to_file) -> object:
        with open(path_to_file) as json_raw:
            json_file = json.load(json_raw)
            return json_file

    def export_file(self, json_obj, path_to_file, rewrite: bool) -> bool:
        with open(path_to_file, "w") as json_file:
            json.dump(json_obj, json_file)
            return True
        return False
