def fibonacci(number):
    if number == 1 or number == 2 :
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

if __name__ == "__main__":
    while True:
        try:
            input_number = int(input("Enter the number of Fibonacic terms you want: "))
            if input_number < 1:
                print("Please enter a positive integer.")
                continue
 
            fibonacci_list = []

            for i in range(1, input_number + 1):
                fibonacci_list.append(fibonacci(i))
            print("Fibonacci sequence:")
            print(", ".join(map(str, fibonacci_list)))
            break


        except ValueError:
            print("Enter (positive) numbers only.")
