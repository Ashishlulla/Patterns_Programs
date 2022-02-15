i = 0
j = 6
for row in range(4):
    for col in range(7):
        if (row == col and col < 4):
            print("*", end=" ")
        elif (row == i and col == j) and (col >3 and col <= 6):
            print("*", end=" ")
            i +=1
            j-=1
        else:
            print(" ", end=" ")
    print()

"""
Output:

*           * 
  *       *
    *   *
      *
      
"""