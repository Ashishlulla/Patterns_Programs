num = int(input("Enter the Number of Row : "))
for row in range(1, num+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print("\n")
"""
Output:
Enter the Number: 5
1         

1 2       

1 2 3     

1 2 3 4   

1 2 3 4 5 

"""

for row in range(num):
    for col in range(row, -1, -1):
        print(col+1, end=" ")
    print("\n")

"""
Output:
Enter the Number: 5
1

2 1

3 2 1

4 3 2 1

5 4 3 2 1
"""

for row in range(1,num+1):
    for col in range(1, row+1):
        print(row, end=" ")
    print("\n")

"""
Output:
1

2 2

3 3 3

4 4 4 4

5 5 5 5 5
"""

for row in range(num):
    for col in range(row+1):
        print(num-row, end=" ")
    print("\n")

"""
Output:
5

4 4

3 3 3

2 2 2 2

1 1 1 1 1
"""

for row in range(num):
    for col in range(row+1):
        print(num-col, end=" ")
    print("\n")

"""
Output:
5

5 4 

5 4 3

5 4 3 2

5 4 3 2 1
"""

for row in range(num):
    for col in range(row, -1,-1):
        print(num-col, end=" ")
    print("\n")

"""
Output:
5

4 5

3 4 5

2 3 4 5

1 2 3 4 5
"""

for row in range(num):
    for col in range(num-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(col+1, end=" ")
    print("\n")

"""
Output:
       1

      1 2

    1 2 3

  1 2 3 4

1 2 3 4 5
"""


for row in range(num):
    for col in range(num-row-1):
        print(" ", end=" ")
    for col in range(row, -1, -1):
        print(col+1, end=" ")
    print("\n")

"""
Output:
        1

      2 1

    3 2 1

  4 3 2 1 

5 4 3 2 1
"""

for row in range(num):
    for col in range(num-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(row+1, end=" ")
    print("\n")

"""
Output:
        1 

      2 2

    3 3 3

  4 4 4 4

5 5 5 5 5
"""

for row in range(num):
    for col in range(num-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(num-row, end=" ")
    print("\n")

"""
Output:
        5

      4 4

    3 3 3

  2 2 2 2

1 1 1 1 1 
"""


for row in range(num):
    for col in range(num-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(num-col, end=" ")
    print("\n")
"""
Output:
        5

      5 4

    5 4 3

  5 4 3 2

5 4 3 2 1

"""
