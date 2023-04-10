#my_files = open("names")
#for line in my_files.readlines():
#    print(line, end='')

# \n = ירידת שורה


def get_name():
    name = input("enter your name:")
    my_files = open("names", "a")
    my_files.write(f"{name}\n")
    my_files.close()


with open("names") as my_files:
    for line in my_files.readlines():
        print(line)


def show_name():
    my_files = open("names")
    for line in my_files.readlines():
        print(f"hello {line}", end='')
    my_files.close()


for i in range(4):
    get_name()
show_name()
