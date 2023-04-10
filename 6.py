a = ["tal", "aliza", "achia"]
if a[0] == "shmulik" or a[1] == "shmulik" or a[2] == "shmulik":
    print("found shmulik")

if "shmulik" in a:
    print("found shmulik")

first_array = []
second_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
if not first_array:
    print("first has no items")
if second_array:
    print("second array has items")
print(len(second_array))
if len(second_array) > 2:
    print("we have at least 3 items in second")

d = 5
g = 10
f = [1, 2, 3]
h = [1, 2, 3]
if d is not g:
    print("d is not g")
if f is h:
    print("f is h")
if type(d) is int:
    print("d is int")