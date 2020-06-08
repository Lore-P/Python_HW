import stringbuilder_class

command_start = "Type your command: add, remove or read"

my_string = stringbuilder_class.StringBuilder()

while True:
    print(command_start)
    input_user = input()
    input_list = input_user.split()
    command = input_list[0]
    if command == "add":
        item = input_list[1] + " "
        my_string.add(item)

    elif command == "remove":
        my_string.remove()

    elif command == "read":
        print(my_string.to_string())

    else:
        print("This action is invalid, please try again.")