for row in range(6):
    for col in range(5):
        if ((col == 0 or col == 4) and (row !=0 and row !=5)) or ((row == 0 or row == 5) and (col > 0 and col < 4)):
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Output:

  0 0 0   
0       0
0       0
0       0
0       0
  0 0 0
  
"""
