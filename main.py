import csv
import req_json_segmnts
import csv_to_json


input_csv = 'req_csv.csv'
jsons = {}

with open(input_csv) as csv_data:
    for row in csv.DictReader(csv_data):
        packageID = row["PACKAGEID"]
        if packageID in jsons:
            csv_to_json.handle_collision(row, jsons[packageID])
        else:
            root = csv_to_json.append_root(row)
            jsons[root["PACKAGEID"]] = root


for key in jsons:
    print(jsons[key])
    print("---------------")