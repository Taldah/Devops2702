result = 0
try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    result = a / b
except ZeroDivisionError as e:
    print("could not divide by zero")
try:
    f = open("blablabla.txt")
except FileNotFoundError as e:
    print("No such file or directory")
except BaseException as e:
    print("something went wrong")
    print(e.args)
print(result)
print("tal")