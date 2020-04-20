#Python.exe C:\Dev\intro\GitHub\HW_4\Python_HW3\Fibonacci_For_Loop\Fib_While.py

fib_index = 3
number = 0
fib_no_at_index = [0, 1]

if number == 0:
    fib_no_at_index[0]
elif number == 1:
    fib_no_at_index[1]
else:
    number = fib_index
    while number <= fib_index:
        new_number = fib_no_at_index[number-3] + fib_no_at_index[number-2]
        fib_no_at_index.append(new_number)
        number += 1