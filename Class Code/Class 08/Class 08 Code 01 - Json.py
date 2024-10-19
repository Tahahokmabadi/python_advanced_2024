import json

file_path = "blah_blah.json"


# text_file = open(file_path)
# print(file_path.read())
# text_file.close()

with open(file_path) as file:
    # print(text_file.read())
    data = json.load(file)

for key, value in data.items():
    print(key)
    print(10 * "_")
    print(value)
    print(10 * "#")



for student in data["students"]:
    print(student["name"])
    print(student["grade"])
    print(10 * "#")