i = 4
j = 3
for row in range(8):
    for col in range(6):
        if (col == 0 and row == 1) or (row == 0 and (col > 0 and col < 4)) or (col == 4 and (row > 0 and row < 4)) or row == 7:
            print("2", end=" ")
        elif (row == i and col == j) and (col > 0 and col < 4):
             print("2", end=" ")
             i +=1
             j -=1
        else:
            print(" ", end=" ")
    print()

"""
Output:
  2 2 2     
2       2
        2
        2
      2
    2
  2
2 2 2 2 2 2
"""
