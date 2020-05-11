# start with creating class and dictionary
command_start = ">command: "
phone_book = {"kelly": 4725692, "lore": 542652}
phone_book_no = {4725692 : "kelly", 542652 : "lore"}

#Create all functions

def add_account(name, number):
    phone_book[name] = number
    phone_book_no[number] = name
    print("The account for %s with number %011d has been added." % (name, int(number)))

def query_no(name, number):
    number = int(input_list[1])
    name = phone_book_no.get(number, "Missing")

    if name == "Missing":
        print("This account is not included in the phonebook, please try again.")
    else:
        print("The number %011d is linked to %s." % (number, name))

def query_name(name, number):
    name = input_list[1]
    name_no = phone_book.get(name, "Missing")

    if name_no == "Missing":
        print("This account is not included in the phonebook, please try again.")
    else:
        print("The number %s is linked to %s." % (name_no, name))


while True:
    print(command_start)
    input_user = input()
    input_list = input_user.split()
    command = input_list[0]
    if command == "add":
        name = input_list[1]
        number = input_list[2]
        add_account(name, number)

    elif command == "query":
        number = input_list[1]
        if number.isdigit():
            query_no(name, number)


        else:
            query_name(name, number)

    else:
        print("This action is invalid, please try again.")

#print(phone_book)