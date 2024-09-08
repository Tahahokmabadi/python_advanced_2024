# even_numbers = [n if n % 2 == 0 else 0 for n in range(1, 11)]
# print(even_numbers)

multiply_two_numbers = lambda number_1, number_2: number_1 * number_2

if __name__ == "__main__":
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))    
    
    result = multiply_two_numbers(number_1, number_2)
    print(result)