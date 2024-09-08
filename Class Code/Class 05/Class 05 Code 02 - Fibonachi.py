def fibonachi(number):
    if number == 1 or number == 2 :
        return 1
    else:
        result = 0
        result = result + (fibonachi(number - 1) + fibonachi(number - 2))
        return result

if __name__ == "__main__":
    input = int(input("Enter: "))
    result = fibonachi(input)

    print(result)
