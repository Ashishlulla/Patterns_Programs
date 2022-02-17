i = 1
j = 4
for row in range(6):
    for col in range(6):
        if row == 0:
            print("7", end=" ")
        elif (row == i and col == j )and ( row > 0 ): 
            print("7", end=" ")
            i +=1
            j -=1
        else:
            print(" ", end=" ")
    print()

"""
Output: 

7 7 7 7 7 7 
        7
      7
    7
  7
7

"""
