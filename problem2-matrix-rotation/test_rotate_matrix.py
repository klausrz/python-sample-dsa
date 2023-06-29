import unittest
from rotate_matrix import rotateMatrix

class TestRotateMatrix(unittest.TestCase):
  def test_empty_matrix(self):
    input = []
    expected = []
    rotated = rotateMatrix(input)
    self.assertEqual(rotated, expected)

  def test_one_by_one_matrix(self):
    input = [[1]]
    expected = [[1]]
    rotated = rotateMatrix(input)
    self.assertEqual(rotated, expected)

  def test_not_squared_matrix(self):
    input = [[1,2,3], [4,5,6], [7,8,9], [10,11,12,13]]
    expected = False
    rotated = rotateMatrix(input)
    self.assertEqual(rotated, expected)

  def test_four_by_four_matrix(self):
    input = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    expected = [[4,8,12,16], [3,7,11,15], [2,6,10,14], [1,5,9,13]]
    rotated = rotateMatrix(input)
    self.assertEqual(rotated, expected)

  def test_three_by_three_matrix(self):
    input = [[1,2,3], [4,5,6], [7,8,9]]
    expected = [[3,6,9], [2,5,8], [1,4,7]]
    rotated = rotateMatrix(input)
    self.assertEqual(rotated, expected)

if __name__ == '__main__':
  unittest.main()

  