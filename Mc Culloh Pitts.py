import numpy as np
def makeMatrix(arr, n):
  l =[]
  for i in range(0, n):
    # print(arr[i], end = " ")
    l.append(arr[i])
  matrix.append(l)

def generateAllBinaryStrings(n, arr, i):
  if i == n:
    makeMatrix(arr, n)
    return
  arr[i] = 0
  generateAllBinaryStrings(n, arr, i + 1)

  arr[i] = 1
  generateAllBinaryStrings(n, arr, i + 1)

# AND gate
print("For And Gate")
col = int(input("Enter the no. of inputs"))
row = pow(2,col)
arr = [None] * col
matrix = [[]]
generateAllBinaryStrings(col,arr,0)
print()
W = np.ones((col,), dtype=int)

for i in range(1,row+1):
  sum = 0
  for j in range(col):
    sum += matrix[i][j]*W[j]
  if sum >= col:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(1)
  else:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(0)


# OR gate
print("For OR Gate")
col = int(input("Enter the no. of inputs"))
row = pow(2,col)
arr = [None] * col
matrix = [[]]
generateAllBinaryStrings(col,arr,0)
print()

T = 1
W = np.ones((col,), dtype=int)
for i in range(1,row+1):
  sum = 0
  for j in range(col):
    sum += matrix[i][j]*W[j]
  if sum >= T:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(1)
  else:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(0)

# NAND gate
print("For NAND Gate")
col = int(input("Enter the no. of inputs"))
row = pow(2,col)
arr = [None] * col
matrix = [[]]
generateAllBinaryStrings(col,arr,0)
print()
W = -1*(np.ones((col,), dtype=int))

for i in range(1,row+1):
  sum = 0
  for j in range(col):
    sum += matrix[i][j]*W[j]
  if sum >= -(col-1):
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(1)
  else:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(0)

# NOR gate
print("For NOR Gate")
col = int(input("Enter the no. of inputs"))
row = pow(2,col)
arr = [None] * col
matrix = [[]]
generateAllBinaryStrings(col,arr,0)
print()
T = 0
W = -1*(np.ones((col,), dtype=int))

for i in range(1,row+1):
  sum = 0
  for j in range(col):
    sum += matrix[i][j]*W[j]
  if sum >= T:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(1)
  else:
    for r in range(col):
      print(matrix[i][r],end = ' ')
    print(0)