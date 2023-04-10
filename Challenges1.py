for row in range(6):
    for col in range(6):
        if (row + col == 5 ) or (row - col == 0):
            print("#",end=" ")
        else:
            print(end="  ")
    print()