my_items = [{"name": "aviel", "age": 33}, {"name": "moshe", "age": 20},
            {"name": "david","age":50}]
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
result = [number / 7 for number in numbers if number > 200]
two_dim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result [curr[1]]
tal = []
for item in my_items:
    tal.append(item["name"])
print(tal)
aa = [item["name"]for item in my_items if item["age"] > 30]
aa = [f"name is: {item['name']}" for item in my_items if item["age"] > 30]
bb = [item["age"]for item in my_items]
print(aa)
print(bb)