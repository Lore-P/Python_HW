#This is the actual budget tracker in which multiple modules will run.

#Open csv file

with open("BankStatement.csv.txt", "r") as f:
    file_data = f.read()


database = {}
temp_input = file_data.replace("\n", ",")
cost_input = temp_input.split(",")

count = len(cost_input)-1
a = 0
b = 0

for x in range(3, count, 3):
    a = x
    b = x + 2
    category = cost_input[b]

    if (x + 2) > count:
        continue

    else:
        if category not in database:
            database[category] = cost_input[a:b]

        else:
            database[category] = database[category] + cost_input[a:b]


# functionality of this module = ask for budget, save budget and print budget
budget_command = "Provide your budget for this month:"

print(budget_command)

budget = input()
result_total_expense = 0

print("Thank you. Your budget for this month is {} GBP.".format(budget))


start_module = "\nThe following commands are valid: \nEnter, will allow you to add data to your expense database; \nDownload, will download a report including your latest expenses by category; \nRemaining, will calculate and print your remaining budget; \nPound, will calculate if you are 'Pound foolish' or 'Penny foolish. \n"
add_costs_command = "When adding your cost to the database, please use the following format: category, name, -amount."

print(start_module)
print(add_costs_command)

command = "\nWhat would you like to do?"


while True:
    print(command)

    total_expense = []

    user_input = input().split(",")

    if user_input[0] == "Enter":
        category = user_input[1]

        if category not in database:
            database[category] = user_input[2:4]
            #Should the amounts be summed by name too?

        else:
            database[category] = database[category] + user_input[2:4]


    elif user_input[0] == "Download":
        for category in database:
            list_amount = []

            if category == "INCOME":
                for x in range(len(database[category])):
                    if x % 2 == 0:
                        continue
                    else:
                        list_amount.append(float(database[category][x]))
                        result = sum(list_amount)

            else:
                for x in range(len(database[category])):
                    if x % 2 == 0:
                        continue
                    else:
                        list_amount.append(float(database[category][x]))
                        total_expense.append(float(database[category][x]))
                        result = sum(list_amount)*-1
                        result_total_expense = sum(total_expense)*-1

            print("Your total expense for %s is %.2f GBP." % (category, result))
        print("Your total expense for this month is %.2f GBP." % (result_total_expense))


    elif user_input[0] == "Remaining":
        income_amount = []
        for x in range(len(database["INCOME"])):
            if x % 2 == 0:
                continue
            else:
                income_amount.append(float(database["INCOME"][x]))
                result_income = sum(income_amount)

        remaining_budget = float(budget) - float(result_total_expense) + float(result_income)
        print("Your remaining budget for this month is %.2f GBP." % (remaining_budget))


    elif user_input[0] == "Pound":
        pound_penny = []
        pound_foolish = []
        penny_foolish = []

        for new_category in database:

            for y in range(len(database[new_category])):

                if y % 2 == 0:
                    continue
                else:
                    pound_penny.append(float(database[new_category][y]))

        for amount in range(len(pound_penny)):
            if pound_penny[amount] < 10:
                penny_foolish.append(pound_penny[amount])
            else:
                pound_foolish.append(pound_penny[amount])

            result_penny = sum(penny_foolish)
            result_pound = sum(pound_foolish)

        if result_penny > result_pound:
            print("You are penny foolish!")
        else:
            print("You are pound foolish!")

    else:
        print("This command is invalid, please try again.")