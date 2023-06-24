from convs.abc_conv import ABCConv


class Ini(ABCConv):

    def import_file(self, path_to_file) -> object:
        #Todo: wenn zahl dann zahl
        with open(path_to_file, "r") as ini_raw:
            ini_file = dict()
            lines = ini_raw.readlines()
            name = None
            for l in lines:
                if not l[-1].isprintable():
                    l = l[:-1]
                l = l.strip()
                if not l:
                    continue
                if l.startswith('['):
                    name = self._create_section(l, ini_file)
                else:
                    if not name:
                        raise Exception
                    key, value = self._create_key_value(l)
                    ini_file[name][key] = value
            return ini_file

    def _create_section(self, line: str, collection: dict):
        name = line.removeprefix('[')
        name = name.removesuffix(']')
        collection[name] = dict()
        return name

    def _create_key_value(self, line: str):
        key_value = line.split("=")
        return key_value[0].strip(), key_value[1].strip()

    def export_file(self, json_obj, path_to_file, rewrite: bool) -> bool:
        pass
