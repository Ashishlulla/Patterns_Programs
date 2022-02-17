i = 0
j = 4
for row in range(4):
    for col in range(8):
        if row == i and  i <= col <= j:
            print("* "*6, end="")
            i +=1
            j +=1
        else:
            print(" ", end="")
    print()

"""
Output:

* * * * * *        
 * * * * * *
  * * * * * *
   * * * * * *
   
"""
