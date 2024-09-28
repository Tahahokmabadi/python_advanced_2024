def khayyam_pascal_triangle(row):
    if row == 0:
        return [1]
    
    previous_row = khayyam_pascal_triangle(row - 1)
    current_row = [1]

    for i in range(1, row):
        current_row.append(previous_row[i - 1] + previous_row[i])
    
    current_row.append(1)

    return current_row


def generate_triangle(number_of_rows):
    triangle = []
    for row in range(number_of_rows):
        triangle.append(khayyam_pascal_triangle(row))
    return triangle

def print_triangle(triangle):
    index = 0
    for row in triangle:
        spaces = " " * (number_of_rows - index - 1)
        print(spaces + " ".join(map(str, row)))
        index += 1
    

if __name__ == "__main__":
    while True:
        try:
            number_of_rows = int(input("Enter the number of rows: "))
            break
        except ValueError:
            print("Enter numbers only.")

    triangle = generate_triangle(number_of_rows)
    print_triangle(triangle)