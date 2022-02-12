string1 = input("Enter the String: ")                                                               
                                                                                                     
for row in range(len(string1)):                                                                            
    for col in range(row+1):                                                                            
        print(string1[row], end=" ")                                                              
    print("\n")                                                               
                                                                               
"""                                                                 
Output:
P 

y y         

t t t       

h h h h     

o o o o o   

n n n n n n 
"""


for row in range(len(string1)):
    for col in range(row+1):
        print(string1[col], end=" ")
    print("\n")

"""
Output:
P 

P y         

P y t

P y t h

P y t h o

P y t h o n
"""

for row in range(len(string1)):
    for col in range(len(string1)-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(string1[row], end=" ")
    print("\n")

"""
Output:
          P

        y y

      t t t

    h h h h

  o o o o o

n n n n n n
"""

for row in range(len(string1)):
    for col in range(len(string1)-row-1):
        print(" ", end=" ")
    for col in range(row+1):
        print(string1[col], end=" ")
    print("\n")

"""
Output:
          P

        P y

      P y t

    P y t h

  P y t h o

P y t h o n
"""

for row in range(len(string1)):
    for col in range(len(string1)-row-1):
        print(" ", end="")
    for col in range(row+1):
        print(string1[row], end=" ")
    print("\n")

"""
Output:
     P

    y y

   t t t

  h h h h 

 o o o o o

n n n n n n
"""

for row in range(len(string1)):
    for col in range(len(string1)-row-1):
        print(" ", end="")
    for col in range(row+1):
        print(string1[col], end=" ")
    print("\n")

"""
Output:
     P

    P y

   P y t 

  P y t h

 P y t h o

P y t h o n
"""


for row in reversed(range(len(string1))):
    for col in range(row+1):
        print(string1[col], end=" ")
    print("\n")

"""
Output:
p y t h o n

p y t h o

p y t h

p y t

p y

p
"""

for row in reversed(range(len(string1))):
    for col in range(row+1):
        print(string1[row], end=" ")
    print("\n")

"""
Output:
n n n n n n

o o o o o

h h h h

t t t

y y

p 
"""

for row in range(len(string1)):
    for col in range(len(string1)-row):
        print(string1[row], end=" ")
    print("\n")

"""
Output:
P P P P P P

y y y y y

t t t t

h h h

o o 

n
"""

for row in range(len(string1)):
    for col in range(row):
        print(" ",end=" ")
    for col in range(len(string1)-row):
        print(string1[col], end=" ")
    print("\n")

"""
Output:
P y t h o n

  P y t h o

    P y t h

      P y t

        P y 

          P
"""

for row in range(len(string1)):
    for col in range(row):
        print(" ",end=" ")
    for col in range(len(string1)-row):
        print(string1[row], end=" ")
    print("\n")

"""
Output:
P P P P P P

  y y y y y

    t t t t

      h h h

        o o

          n
"""


for row in range(len(string1)):
    for col in range(row):
        print(" ",end="")
    for col in range(len(string1)-row):
        print(string1[col], end=" ")
    print("\n")

"""
Output:
P y t h o n 

 P y t h o

  P y t h

   P y t

    P y

     P
"""

for row in range(len(string1)):
    for col in range(row):
        print(" ",end="")
    for col in range(len(string1)-row):
        print(string1[row], end=" ")
    print("\n")

"""
Output:
P P P P P P

 y y y y y

  t t t t

   h h h

    o o

     n
"""

for row in reversed(range(len(string1))):
    for col in range(len(string1)-row):
        print(" ", end=" ")
    for col in range(row+1):
        print(string1[row],end=" ")
    print("\n")
"""
n n n n n n

    o o o o o

      h h h h

        t t t

          y y

            P 
"""

for row in reversed(range(len(string1))):
    for col in range(len(string1)-row):
        print(" ", end=" ")
    for col in range(row,-1,-1):
        print(string1[col],end=" ")
    print("\n")

"""
Output:
 n o h t y P

    o h t y P

      h t y P 

        t y P

          y P

            P
"""
