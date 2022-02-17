for row in range(4):
    for col in range(4):
        if (col == 0 or col == 3) or ((row == 0 or row == 3) and (col > 0 and col < 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Output:

* * * * 
*     *
*     *
* * * *

"""
