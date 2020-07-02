#Open csv file

with open("BankStatement.csv.txt", "r") as f:
    file_data = f.read()


database = {}
temp_input = file_data.replace("\n", ",")
cost_input = temp_input.split(",")

count = len(cost_input)-1
print(count)

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

print(database)

