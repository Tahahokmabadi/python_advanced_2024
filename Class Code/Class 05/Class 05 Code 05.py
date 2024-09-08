power = lambda number: number ** 2 if number % 2 == 0 else number ** 3

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(power(number))
