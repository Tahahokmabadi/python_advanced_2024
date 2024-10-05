ages = list(input("Enter numbers separated by space: ").split())

def even_spliter(ages):
    for age in ages:
        if int(age) % 2 == 0:
            return True
        else:
            return False

result = filter(even_spliter, ages)
print(list(result))
