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
