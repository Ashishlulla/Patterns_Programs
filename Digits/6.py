for row in range(8):
    for col in range(5):
        if (col == 0 and (row != 0 and row!=7)) or ((row == 0 or row == 3 or row ==7)and(col > 0 and col < 4)):
            print("6",end=" ")
        elif (col == 4 and (row > 3 and row < 7 or row == 0)):
            print("6",end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Output:
  6 6 6 6 
6
6
6 6 6 6
6       6
6       6
6       6
  6 6 6 
"""
