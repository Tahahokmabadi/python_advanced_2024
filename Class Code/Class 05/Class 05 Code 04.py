fruit_1 = input("Enter the first fruit: ")
fruit_2 = input("Enter the second fruit: ")

juice_maker = lambda fruit_1, fruit_2: (f"{fruit_1} {fruit_2} juice")

print(juice_maker(fruit_1, fruit_2))