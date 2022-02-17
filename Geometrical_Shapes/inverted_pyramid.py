for row in range(4, -1,-1):
    for col in range(4-row+1):
        print(" ",end="")
    for col in range(row+1):
        print("*",end=" ")
    print()

"""
Output

 * * * * * 
  * * * *
   * * *
    * *
     *

"""
