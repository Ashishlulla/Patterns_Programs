i = 6
j = 12

for row in range(12):
    for col in range(14):
        if ( row == 0 and ( 1 < col < 5  or  9 < col < 13)) or ((col == 1 or col == 13) and (row > 0 and row < 6)) or (col - row == 4 and (4 < col < 8)) or (row == 1 and col == 9) or (row == 2 and col == 8) or (row - col == 4 and (0 < col < 8)):
            print("*", end=" ")
        elif ((row == i and col == j) and (7 < col < 13)):
            print("*", end=" ")
            i += 1
            j -= 1
        else:
            print(" " ,end=" ")
    print(" ")

"""
Output:

    * * *           * * *    
  *       *       *       *  
  *         *   *         *  
  *           *           *  
  *                       *  
  *                       *  
    *                   *    
      *               *      
        *           *        
          *       *
            *   *
              *

"""
