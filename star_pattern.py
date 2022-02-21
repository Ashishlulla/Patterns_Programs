i = 2
j = 7

a = 5 
b = 15
for row in range(13):
    for col in range(17):
        if ((row == 4 or row == 9) and (col !=5 and col != 11))  or (col-row == 7 and (7 < col)) or (row - col == 4 and (0 <= col < 8)):
            print("*", end=" ")
        elif (row == i and col == j) and (0 <= col < 8 ):
            print("*", end=" ")
            i +=1
            j -=1
        elif (row == a and col == b) and (7 <= col < 16):
            print("*", end=" ")
            a +=1
            b -=1
        else:
            print(" ", end=" ")
    print()
        

"""
Output:


                *
              *   *
            *       *
* * * * * * * * * * * * * * * * *
  *     *               *     *
    * *                   * *
    * *                   * *
  *     *               *     *
* * * * * * * * * * * * * * * * *
            *       *
              *   *
                *

"""
