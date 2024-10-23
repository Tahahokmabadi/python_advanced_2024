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

'''
def print_centered_triangle(triangle):
    index = 0

    for row in triangle:
        spaces = " " * (number_of_rows - index - 1)
        print(spaces + " ".join(map(str, row)))
        index += 1
'''    

def print_absolutely_centered_triangle(triangle):
    max_num = max(max(row) for row in triangle)
    max_len = len(str(max_num))

    last_row = " ".join(f"num:{max_len}" for num in triangle[-1])
    total_len = len(last_row)
    
    for row in triangle:
        # row_string = " ".join(map(str, row))
        

        row_string = " ".join(f"{num:{max_len}}" for num in row)

        number_of_spaces = (total_len - len(row_string)) // 2
        number_of_spaces += (total_len - len(row_string)) % 2
        centered_row = " " * number_of_spaces + row_string
        print(centered_row)

if __name__ == "__main__":
    while True:
        try:
            number_of_rows = int(input("Enter the number of rows: "))
            if number_of_rows < 1:
                print("The number of rows can't be lower than 1.")
                continue
            break
        
        except ValueError:
            print("Enter numbers only.")

    triangle = generate_triangle(number_of_rows)
    # print_triangle(triangle)
    print_absolutely_centered_triangle(triangle)
