while True:  
  try:
    import random
    Tie = 0
    def printboards(x,y):
      for i in range(y):
          print (x*"| | ")
          print (x*" _  ")
    boardX = 3
    boardY = 3
    printboards(boardX, boardY)
    if boardX != boardY:
      Diagonal = False
    Matrix = [[0-0 for x in range(boardX)] for y in range(boardY)]
    Matrix_2 = [[" "for x in range(boardX)] for y in range(boardY)]
    l = len(Matrix)
    length_q = 0
    for r in range(len(Matrix)):
      length_q = length_q + len(Matrix[r]) 
    length_q = (length_q / len(Matrix))
    def turnX(Tie):
      C1_row = int(random.randint(1, boardX))
      C1_row = C1_row - 1
      C1_column = int(random.randint(1, boardY))
      C1_column = C1_column - 1
      if (1 == Matrix[C1_column][C1_row] or 500 == Matrix[C1_column][C1_row]):
          return turnX(Tie)
      else:
          print ("Computer 1's Turn:")
          Matrix[C1_column][C1_row] = 1
          Matrix_2[C1_column][C1_row] = "X"
          return Tie + 1
    def turnY(Tie):
      C2_row = int(random.randint(1, boardX))
      C2_row = C2_row - 1
      C2_column = int(random.randint(1, boardY))
      C2_column = C2_column - 1
      if (1 == Matrix[C2_column][C2_row] or 500 == Matrix[C2_column][C2_row]):
          return turnY(Tie)
      else:
        print ("Computer 2's Turn:")
        Matrix[C2_column][C2_row] = 500
        Matrix_2[C2_column][C2_row] = "O"
        return Tie + 1
    def printArray(boardX, boardY):
      for i in range(boardX):
          print ("")
          for j in range(boardY):
              print ("|", Matrix_2[i][j],"| ",)
    win = False
    def win_condition():
        row = [sum(row) for row in Matrix]
        result = [sum(row[i] for row in Matrix) for i in range(len(Matrix[0]))]
        diagonal1 = [sum(Matrix[i][i] for i in range(l))]
        diagonal2 = [sum(Matrix[l-1-i][i] for i in range(l-1,-1,-1))]
        result = [sum(row[i] for row in Matrix) for i in range(len(Matrix[0]))]
        for h in range(0, boardX):
          if row[h] == length_q * 500:
            print ("Computer 2 wins!")
            win = True
            printArray(boardX, boardY)
            quit()
            printArray(boardX, boardY)
          if row[h] == length_q:
            print ("Computer 1 wins!")
            win = True
            printArray(boardX, boardY)
            quit()      
          for e in range(0, boardY):
            if result[e] == boardY * 500:
              print ("Computer 2 wins!")
              win = True
              printArray(boardX, boardY)
              quit()
              printArray(boardX, boardY)
            if result[e] == boardY:
              print ("Computer 1 wins!")
              win = True
              printArray(boardX, boardY)
              quit()
              printArray(boardX, boardY)
        if diagonal1[0] == length_q:
          print ("Computer 1 wins!")
          win = True
          printArray(boardX, boardY)
          quit()
        if diagonal1[0] == length_q * 500:
          print ("Computer 2 wins!")
          win = True
          printArray(boardX, boardY)
          quit()
        if diagonal2[0] == length_q:
          print ("Computer 1 wins!")
          win = True
          printArray(boardX, boardY)
          quit()
        if diagonal2[0]== length_q * 500:
          print ("Computer 2 wins!")
          win = True
          printArray(boardX, boardY)
          quit()
    while Tie != boardX * boardY:
        Tie = turnX(Tie)
        win_condition()
        printArray(boardX, boardY)
        Tie = turnY(Tie)
        win_condition()
        printArray(boardX, boardY)
    if Tie == boardX * boardY:
      print ("It's a tie!")
      quit()
    break
  except RuntimeError:
    print ("It's a tie!")
