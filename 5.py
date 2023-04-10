isTrue = False
a = True
b = 2.5
strOne = "One"
strThree = "Three"

is_today_a_good_day = a > b and (strOne == "tal" or b > 1)
if is_today_a_good_day:
    print("a is greate then b")
elif (not a) == b:
    print("a equals then b")
elif strOne != strThree:
    print("blabla")
else:
    print("b is greater then a")