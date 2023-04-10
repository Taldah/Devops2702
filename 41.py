# importing the module
import ast

# reading the data from the file
with open('dip.txt') as f:
    data = f.read()

print("Data type before reconstruction : ", type(data))
#print(data)

# reconstructing the data as a dictionary
d = ast.literal_eval(data)

print("Data type after reconstruction : ", type(d))
print(f"name: {d['name']}, age: {d['age']}")