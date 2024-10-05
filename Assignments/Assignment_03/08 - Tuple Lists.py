while True:
    try:
        number_of_tuple = int(input("Enter the number of tuples: "))
        break
    except ValueError:
        print("Only numeric values are acceptable. Try again...")


list_of_tuples = []


for i in range (number_of_tuple):
    while True:
        try:
            tuples = input(f"Enter the values for the #{i + 1} tuple seperated by a space (a b): ")
            a, b = map(int, tuples.split())
            list_of_tuples.append((a, b))
            break
        except ValueError:
            print("Only numeric values are acceptable. Try again...")
            continue
         
reault = sorted(list_of_tuples, key=lambda x: x [1])
print(reault)