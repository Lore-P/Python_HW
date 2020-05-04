# start with creating class and dictionary


class MyPhonebook:
    phonebook = {}
    
    def my_command(self): #ask for command
        print("> Command:\n")
    def add_person(self, name, number):  #add person
        name = name
        self.phonebook[name] = number
        return "%s with number %d has been added to the phonebook." % (name, number)
    def query_name(self, name): #look for person in dictionary
        if name in self.phonebook.item():
            print(" %s 's number is %d. \n >Command:" % (name, number))
        else:
            print("This person is not included in the phonebook. Please add the person to the phonebook and try again. \n >Command:")
    def query_number(self, number): #look for number in dictionary  
        if number in phonebook.item():
            print(" %s 's number is %d. \n >Command:" % (name, number))
        else:
            print("This number is not included in the phonebook. Please add the number to the phonebook and try again. \n >Command:")    
            
            
my_phone_book = MyPhonebook()
my_phone_book.add_person('Peter', 5643764753563)
