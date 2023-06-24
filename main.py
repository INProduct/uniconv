from convs import conv_xml
from convs import conv_csv
from convs import conv_json
from convs import conv_ini


xml_conv = conv_xml.Xml()
csv_conv = conv_csv.Csv()
json_conv = conv_json.Json()
ini_conv = conv_ini.Ini()

if __name__ == '__main__':
    # print(csv_conv.import_file("tests/test_csv.csv"))
    # print(json_conv.import_file("tests/test_json.json"))
    # print(xml_conv.import_file("tests/test_xml.xml"))
    get_ini = ini_conv.import_file("tests/test_ini.ini")
    json_conv.export_file(get_ini, "tests/new_json.json", True)
