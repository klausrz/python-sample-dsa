def printArray(a: list[list[int]]) :
  size = len(a)
  for i in range(size):
    print(a[i])

def rotateMatrix(matrix : list[list[int]]) -> list[list[int]]:
  n = len(matrix)
  if n == 0:
    return []

  # init n x n matrix and fill with None
  rotated = [[None] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      # do the rotation
      rotated[i][j] = matrix[j][n - 1 - i]

  return rotated

