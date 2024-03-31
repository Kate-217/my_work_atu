import my_functions

nTimes = int(input('how many:'))
try:
    print(my_functions.fibonacci(nTimes))
except ValueError:
    print("value error")
