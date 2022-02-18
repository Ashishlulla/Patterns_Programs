i = 3
j = 14
for row in range(17):
    for col in range(40):
        if (row == 2 and ( col > 14 and col < 25)) or (row == 8 and(col > 3 and col < 35)) or (row == 13 and (col != 8 and col != 9 and col != 10 and col != 30 and col != 31 and col != 32)) or ((row ==12 or row ==14 ) and (col == 7 or  col == 10 or col == 29 or col == 32)) or ((row == 11 or row == 15 ) and (col == 8 or col == 9 or col == 30 or col == 31)) or (col == 19 and (row > 1 and row < 9))or((row == col - 22) and (row > 1 and row < 9)) or (row == col - 26 and (row > 8 and row < 13)) or (row == 9 and col == 3) or(row == 10 and col == 2) or(row == 11 and col == 1) or (row == 12 and col == 0) or row == 16:
            print("*", end=" ")
        elif (row == i and col == j) and (col > 8 and col < 15):
            print("*", end=" ")
            i += 1
            j -= 1

        else:
            print(" ",end=" ")
    print()

"""
Output:



                              * * * * * * * * * *
                            *         *           *
                          *           *             *
                        *             *               *
                      *               *                 *
                    *                 *                   *
      * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    *                                                                 *
                                                                        *
  *             * *                                         * *           *
              *     *                                     *     *           *
* * * * * * * *       * * * * * * * * * * * * * * * * * * *       * * * * * * *
              *     *                                     *     *
                * *                                         * *

"""
