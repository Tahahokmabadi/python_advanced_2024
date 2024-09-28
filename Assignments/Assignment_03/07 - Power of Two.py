def power_of_two(number_list):
    squared = list(map(lambda x: x ** 2, number_list))
    print(f"Here are the numbers to the power of two:\n{squared}")

if __name__ == "__main__":
    
    while True:
        try:
            number_list = list(input("Enter numbers seperated by space: ").split())
            number_list = [int(number) for number in number_list]
            break
        except ValueError:
                print('Enter numbers seperated by space only.')
    
    power_of_two(number_list)