while True:
    try:
        list_1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
        list_2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))
    except ValueError:
        print("Please enter numbers seperated by space only.")
        continue
    
    if len(list_1) != len(list_2):
        print("Both lists must be the same size.")
        continue
    
    sum_list = list(map(lambda x, y: x + y, list_1, list_2))
    print(f"New list:\n{sum_list}")

