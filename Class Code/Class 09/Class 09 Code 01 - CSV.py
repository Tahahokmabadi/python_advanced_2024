import csv

path = ".../employees.csv"


with open(path, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)

    headers = next(reader)

    for row in reader:
        print(row)
