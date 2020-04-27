# start with creating class and dictionary
x = ">command: "
phone_book = {"kelly": 4725692, "lore": 542652}
name = ""
number = 0
print(x)


y = input()
new_list = y.split()
#print(new_list)

for word in new_list:
    if word == "add":
        name = new_list[1]
        number = new_list[2]
        phone_book[name] = number
        print("this has been added \n", x)
    elif word == "query":
        name = new_list[1]
        for name in phone_book.items():
            print("this is included")
    else:
        print(">command: ")

#print(phone_book)