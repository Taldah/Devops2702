names = ["inbar", "lanir", "tal", "eran", "alina"]
#numbers = [1, 2, 3, 4, 5, 6, 7]
 #   name = "noa"
 #   print(name)
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
     if number == 3:
         continue
     if number == 2:
         break
     print(number)
else:
     print("finished successfully")

for i in range(len(names)):
    #print(names[i])
    names[i] = "noa"

for name in names:
    print(name)
a = 0
while a < 5:
    print(a)
    a += 1
else:
    print("finished")