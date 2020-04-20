#Python.exe C:\Dev\intro\GitHub\HW_4\Python_HW3\Fibonacci_For_Loop\Fib_For.py

# index number that will be run through the formula
fib_index = 5
fib_no_at_index = [0,1]

#create Fibonacci For-loop
for number in range(3,fib_index):
    if number == 0:
        fib_no_at_index[0]
    elif number == 1:
        fib_no_at_index[1]
    else:    
        new_number = fib_no_at_index[number-3] + fib_no_at_index[number-2]
        fib_no_at_index.append(new_number)
print(fib_no_at_index)

