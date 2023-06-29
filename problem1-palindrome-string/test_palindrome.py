import unittest
from is_palindrome_string import isPalindrome

class TestPalindrome(unittest.TestCase):
  def test_one_char_string(self):
    self.assertTrue(isPalindrome("1"))
  
  def test_non_alphanumeric(self):
    self.assertTrue(isPalindrome("**$$**)()#"))

  def test_not_palindrome_string(self):
    self.assertFalse(isPalindrome("nopalindrome"))

  def test_empty_string(self):
    self.assertTrue(isPalindrome(" "))

  def test_valid_palindrome_tring(self):
    self.assertTrue(isPalindrome("madam&$was$it$a$car$or$a$cat$I$saw&madam&$"))

  def test_valid_palindrome_tring2(self):
    self.assertTrue(isPalindrome("racecar"))

if __name__ == '__main__':
  unittest.main()

  