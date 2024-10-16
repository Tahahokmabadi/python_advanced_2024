import json

# print("Start")

file_path = "Assignments\\Assignment_06\\apple.json"

with open(file_path) as file:
    data = json.load(file)

key_name_list = ["sector", "fullTimeEmployees", "longBusinessSummary", "city", "country", "phone"]

for key_name in key_name_list:
    for key in data.keys():
        if key == key_name:
            print(f"{key_name}: {data[key_name]}\n")

# print("end")
