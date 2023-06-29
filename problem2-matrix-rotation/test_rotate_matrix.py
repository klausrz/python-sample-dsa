import unittest
from rotate_matrix import rotateMatrix

class TestRotateMatrix(unittest.TestCase):
  def test_one_char_string(self):
    input = [[1,2,3], [4,5,6], [7,8,9]]
    expected = [[3,6,9], [2,5,8], [1,4,7]]
    rotated = rotateMatrix(input)
    self.assertEqual(rotated, expected)

if __name__ == '__main__':
  unittest.main()

  