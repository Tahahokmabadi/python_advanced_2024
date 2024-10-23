import csv


def cal_sum(file_path):
    sum = 0
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            sum += float(row[3])
    return sum    

if __name__ == "__main__":
    file_path = "Assignments\\Assignment_07\\Example file (14)\\expenses.csv"
    total_expenses = cal_sum(file_path)
    print(f"Total Expenses: {total_expenses}")
