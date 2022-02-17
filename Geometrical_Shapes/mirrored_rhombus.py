i = 0
j = 3
for row in range(4):
    for col in range(7):
        if row == i and col ==  j:
            print("* "*4, end=" ")
            i +=1
            j -=1
        else:
            print(" ", end=" ")
    print() 

"""
Output:

      * * * *        
    * * * *
  * * * *
* * * *

"""
