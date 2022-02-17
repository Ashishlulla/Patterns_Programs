i = 0
j = 2
for row in range(6):
    for col in range(5):
        if (col == 2 and row !=0) or row == 5:
            print("1", end=" ")
        elif ((row == i and col == j)and col < 3):
            print("1", end=" ")
            i +=1
            j -=1
        else:
            print(" ", end=" ")
    print()

"""
Output:

    1     
  1 1
1   1
    1
    1
1 1 1 1 1

"""
