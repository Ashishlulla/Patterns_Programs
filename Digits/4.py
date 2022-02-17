i = 1 
j = 3
for row in range(7):
    for col in range(7):
        if col == 4 or row == 4:
            print("4", end=" ")
        elif ((row == i and col == j)and (col > 0)):
            print("4", end=" ")
            i +=1
            j -=1
        else:
            print(" ", end=" ")
    print()


"""
Output:

        4     
      4 4
    4   4
  4     4
4 4 4 4 4 4 4
        4
        4
        
"""
