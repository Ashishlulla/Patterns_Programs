i = 0
j = 6
for row in range(7):
    for col in range(7):
        if ((col == row) and col>=0 and col < 4) or (col == 3 and row > 3):
            print("*", end=" ")
        elif (row == i and col == j):
            print("*", end=" ")
            i +=1
            j -=1
        else:
            print(" ", end=" ")
    print()


"""
Output:

*           * 
  *       *
    *   *
      *
      *
      *
      *
      
"""