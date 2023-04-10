c = 6
try:
    a = 10 / 0
except ZeroDivisionError as d:
  print("could not divide by zero")
  print(d.args)
print(c)
print("hello")


try:
    x = 1 / 0
except ZeroDivisionError as d:
    print("could not divide by zero")
    print(d.args)
finally:
    print("finally")

def createfile():
 name = input("enter your name:")
 my_file = open(r"C:\\Users\\taltech\\PycharmProjects\\Devops2702\\words.txt", 'w', encoding='utf-8' )
 my_file.write(f"{name}\n")

 with open("words.txt", encoding='utf-8') as my_file:
     for line in my_file.readlines():
         print(line)
 my_file.close()


#for i in range(1):
createfile()

