i = 11
j = 13

a = 10
b = 2
for row in range(18):
    for col in range(22):
        if ((row == 6 or row == 10) and ( 4 < col < 9 or 13 < col < 20)) or ((col == 3 or col == 20) and (6<row<10)) or (col == 9 and (0 < row < 7 or 9 < row < 16)) or ((row == 3 or row == 13) and (col < 3)) or (row == col - 8) and (9 < col < 14) or (row == col + 1 and (2 < col < 5)) or (row - col == 4 and (col < 3)) or(row == 11 and col == 4) or (row == 12 and col == 3) or (col == 21 and row == 8):
            print("*" ,end="  ")
        elif (row == i and col == j) and ( 9 < col < 14):
            print("*", end="  ")
            i +=1
            j -=1
        elif (row ==a and col == b) and (col < 3):
            print("*", end="  ")
            a +=1
            b -=1
        else:
            print(" ", end="  ")
    print()

   
"""
                           *
                           *  *
*  *  *                    *     *
*        *                 *        *
   *        *              *           *
      *        *  *  *  *  *              *  *  *  *  *  *
         *                                                  *     
         *                                                     *
         *                                                  *
      *        *  *  *  *  *              *  *  *  *  *  *        
   *        *              *           *
*        *                 *        *
*  *  *                    *     *
                           *  *
                           *

"""
