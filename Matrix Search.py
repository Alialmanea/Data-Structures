import numpy as np


def contains(matrix, n):
  rows = len(matrix)
  cols = len(matrix[0])

  if rows == 0 and cols == 0:
    return False
  rows  = 0  
  cols = len(matrix) - 1

  while(rows < len(matrix) and cols >= 0):
    if matrix[rows, cols ] == n :
      return True
    elif matrix[rows, cols] <  n:
      rows += 1
    else :
      cols -= 1   
  
  return False


def main():
  matrix = np.zeros((3, 3))
  k = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      k += 1
      matrix[i, j] = k 

  print(matrix)  
  print(contains(matrix, 1))  



main()
