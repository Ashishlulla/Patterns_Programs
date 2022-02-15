i1 = 0
j1 = 6

i2 = 0 
j2 = 12
for row in range(4):
    for col in range(13):
        if (row == col and col < 4) or (col == 7 and row == 1) or (col == 8 and row == 2):
            print("*", end=" ")
        elif (row == i1 and col == j1) and (col >3 and col <= 6):
            print("*", end=" ")
            i1 += 1
            j1 -= 1
        elif (row == i2 and col == j2) and (col > 8 and col <= 12):
            print("*", end=" ")
            i2 += 1
            j2 -= 1
        else:
            print(" ", end=" ")
    print()


"""
Output:

*           *           * 
  *       *   *       *
    *   *       *   *
      *           *   
      
"""