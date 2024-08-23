valid_number = []
for i in range (10):
    valid_number.append(str(i))

while True:
    age = input("Please enter your age:\t")
    if age == "quit":
        break

    for char in age:
        if char not in valid_number:
            raise ValueError("Enter numbers only.")


    # try:
    #     age = int(age)
    #     if age >= 18:
    #         print("You can vote.")
    #     else:
    #         print("You can't vote.")
    # except ValueError as e:
    #     print(f"bad input.\nYour error is {e}.")
    # except Exception as e:
    #     print(e)
    # else:
    #     print("The program ran successfully.")


    # finally:
    #     print("The end.")
# try:
#     print(name)
# except:
#     print("bad input")
