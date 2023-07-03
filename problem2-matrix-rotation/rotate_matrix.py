def rotateMatrix(matrix : list[list[int]]) -> list[list[int]]:
  n = len(matrix)
  if n == 0:
    return []

  # the input is not a n_by_n matrix
  if not len(matrix[0]) == n:
    return False

  # init n x n matrix and fill with None
  rotated = [[None] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      # do the rotation
      rotated[i][j] = matrix[j][n - 1 - i]

  return rotated



def rotateMatrix2(matrix : list[list[int]]) -> list[list[int]]:
  n = len(matrix)
  if n == 0:
    return []

  # the input is not a n_by_n matrix
  if not len(matrix[0]) == n:
    return False

  # init n x n matrix and fill with None
  # rotated = [[None] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      # do the rotation
      temp = matrix[i][j]
      matrix[i][j] = matrix[j][n - 1 - i]
      matrix[j][n - 1 - i] = temp
  return matrix

#  O( 3(n * n) ) => O(n * n) 




