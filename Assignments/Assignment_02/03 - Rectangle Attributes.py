def rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def rectangle_area(length, width):
    area = (length * width)
    return area   


if __name__ == "__main__":
    while True:
        try:
            length = float(input("Enter the length of the rectangle:\t"))
            width = float(input("Enter the width of the rectangle:\t"))
            print("_" * 30)

            perimeter = rectangle_perimeter(length, width)
            area = rectangle_area(length, width)

            print(f"The length of the rectangle: {length}\nThe width of the rectangle: {width}\n")
            print(f"The perimeter of the rectangle: {perimeter}")
            print(f"The area of the rectangle: {area}")

            break
        
        except ValueError:
            print("Only numeric values are accepted.")
            continue
        
        except Exception as e:
            print(f"\nAn error has occured:\n{e}")
            continue
