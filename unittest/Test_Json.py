import unittest
from convs.conv_json import Json


class TestJsonConv(unittest.TestCase):

    def setUp(self) -> None:
        self.json_conv = Json()

    def test_import_file_success(self):
        obj = self.json_conv.import_file("../tests/test_json.json")
        self.assertNotEqual(obj, None)
        print(obj)

    def test_import_file_error_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            obj = self.json_conv.import_file("./tests/test_json.json")
            print(obj)





if __name__ == '__main__':
    unittest.main()
