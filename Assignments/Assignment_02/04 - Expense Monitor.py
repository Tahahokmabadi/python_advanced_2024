print(f"Hello there!\nThis program will monitor your expense(s) and income(s).")

currency = ""

expenses_dict = {}


def add_expense (expense, amount):
    amount = float(amount)
    if expense in expenses_dict:
        amount += float(expenses_dict[expense])
    expenses_dict[expense] = float(amount)

def sum_of_expenses ():
    sum = 0
    for key in expenses_dict:
        sum += float(expenses_dict[key])
    return float(sum)

def budget_sum (budget):
    budget = float(budget)
    sum = sum_of_expenses()
    budget -= sum

    if budget > 0:
        bankruptcy = False
    elif budget < 0:
        bankruptcy = True
    else:
        bankruptcy = None

    return budget, bankruptcy

def set_currency (new_currency):
    currency = new_currency


while True:
    print(f"1. Add New Expense\n2. Show Sum of Expenses\n3. Set Budget (income)\n4. Show Sum of Budget\n5. Set Currency\n6. Exit program")
    action = input("Enter the number of the action you want to perform:\t")

    if action.isdigit() is False:
        print("Enter numeric values only.")
        continue
    if (1 > int(action)) or (int(action) > 6):
        print("Enter numbers between 1 to 6 only.")
        continue
    action = int(action)

    if int((str(action).strip())) == 1:
        expense = input("Enter the type of your expense:\t")
        amount = input("Enter the amount you have spent:\t")
        add_expense(expense, amount)
        print("Done!")
        continue

    elif int((str(action).strip())) == 2:
        sum = sum_of_expenses()
        print(f"The sum of your expenses is {sum} {currency}.")
        continue

    elif int((str(action).strip())) == 3:
        while True:
            budget = input("Enter your budget:\t")
            if budget.isdigit() is False:
                print("Enter numeric values only.")
                continue
            budget = float(budget)
            print(f"Your budget: {budget}")
            break
        

    elif int((str(action).strip())) == 4:
        budget_sum, bankruptcy = budget_sum(budget)
        print(f"Your total budget minus the expenses: {budget_sum}")
        if bankruptcy == True:
            print("Your expenses have surpassed your budget (income).\nBe careful not to go bankrupt!")
        elif bankruptcy == None:
            print("You have spent all of your budget.\nBe careful not to go bankrupt!")
        continue        

    elif int((str(action).strip())) == 5:
        set_currency(input("Enter your desired currency:\t"))
        print("Done!")
        continue

    elif int(action) == 6:
        print("Thank you for using our program.")
        break
