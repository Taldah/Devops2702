def get_name():
    current_age = int(input("enter your age: "))
    if current_age < 0:
        raise BaseException("age can not be negative", current_age)
    else:
        print(f"your age is ligel {current_age}")
try:
    get_name()
except BaseException as e:
    print(e.args)