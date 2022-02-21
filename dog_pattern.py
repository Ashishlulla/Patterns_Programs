for row in range(26):
    for col in range(33):
        if ((row == 4 or  row == 16) and (6 < col < 12 or 18 < col < 24 or 28 < col < 32)) or (col == 32 and (4<row<8 or 8<row<12 or 16<row<20 or 20<row<24)) or ((col == 7 or col == 19) and (3 < row < 9 or 15 < row < 21)) or ((row == 8 or row == 12 or row == 20 or row == 24) and (6 < col < 11 or 18 < col < 23 or 28 < col < 32)) or ((col == 11 or col == 23) and (8<row<12 or 20<row<24)) or (col - row == 7 and (11 < col < 19)) or (row - col == 5 and (11 < col < 19)) or (col == 28 and (12<row<16))or(col - row == 5 and (26 <col < 29)) or (col - row == 7 and (23<col<26)) or (col == 26 and( 18< row < 22)) or ((col == 23 or col == 28) and (row == 2 or row == 3)) or (row == 1 and ( 23 < col < 28)) or (row == 10 and ( 2 < col < 6)) or (col == 6 and row == 11) or (col == 0 and ( 12 < row < 18)) or (row == col + 17 and (col < 7))or (col == 1 and row == 12) or  (row ==11 and col == 2) or (row == 6 and (23<col<29 and col != 25 and col !=27)) or (row == 5 and 24 < col < 28):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


"""
Output:


                                                * * * *
                                              *         *
                                              *         *
              * * * * *               * * * * *           * * *   
              *         *             *           * * *         * 
              *           *           *         *   *   *       * 
              *             *         *                         * 
              * * * *         *       * * * *             * * *   
                      *         *             *                 * 
      * * *           *           *           *                 * 
    *       *         *             *         *                 * 
  *           * * * *                 * * * *             * * *   
*                                                       *
*                                                       *
*                                                       *
*             * * * * *               * * * * *           * * *   
*             *         *             *         *               * 
  *           *           *           *           *             * 
    *         *             *         *             *           * 
      *       * * * *         *       * * * *       *     * * *   
        *             *         *             *     *           *
          *           *           *           *       *         *
            *         *             *         *         *       *
              * * * *                 * * * *             * * *

"""
