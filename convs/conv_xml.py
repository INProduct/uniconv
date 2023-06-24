from convs.abc_conv import ABCConv
import xml.etree.ElementTree as et


class Xml(ABCConv):

    def import_file(self, path_to_file):
        tree = et.parse(path_to_file)
        root = tree.getroot()
        # print("root.getchildren ", root.getchildren())
        for child in root:
            it = child.items()
            print(child.tag, child.attrib)
            for c in child:
                print("len(c) ", len(c))
                print(c.tag, c.attrib, c.text)
                for b in c:
                    print(b.tag)

    def export_file(self, json_obj, path_to_file, rewrite: bool) -> bool:
        return False
