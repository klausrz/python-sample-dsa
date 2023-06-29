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

