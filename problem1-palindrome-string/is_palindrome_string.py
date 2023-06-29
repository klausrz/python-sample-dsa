# Palindrome String DEFINITION:
# A string is a palindrome if the string read from left to right
# is equal to the string read from right to left, IGNORING the 
# difference between uppercase and lowercase letters, and EXCLUDE
# all non-alphanumeric characters

# APPROACH:
# We'll be using two pointers, each starts at each end of the string
# At each iteration, the pointers move towards the opposite direction
# until they meet at the middle of the string

# At each iteration of the loop, the characters at the two pointers
# will be checked if they're alphanumeric or not. If not, the pointer
# will be moved one step to the left or right. If the two characters are 
# alphanumeric, they will be converted to lowercase before being compared.
# In case of equal, move both pointers one step to left and right. In case of 
# not equal, the string is not a Palindrome

# The loop stops when the "start" pointer is greater than the "end" pointer
# At this time, we can conclude that the string is a Palindrome

# I'm using Python as it is my favourite programing language
# for solving Data Structure and Algorithm problems

def isPalindrome(s: str)  -> bool :
  length = len(s)
  if length == 1:
    return True
  first, last = 0, length - 1
  while first < last and first < length - 1 and last >= 0:
    # only check alpha numeric characters, ignore others
    while first < length and not s[first].isalnum() :
      first += 1
    while last >= 0 and not s[last].isalnum():
      last -= 1

    # there's no alpha numeric characters
    if first > length or last < 0 : 
      return True
    
    if not s[first].lower() == s[last].lower():
      return False
    first += 1
    last -= 1
    
  return True
  

# time complexity: O(n)

# We'll be using two pointers, each starts at each end of the string
# At each iteration, the pointers move towards the opposite direction
# until they meet at the middle of the string
# As a result, each character of the input string will be visisted once 
# even in worst cases
# Although we have nested loops, the inner loop only checks if a character
# is alpha numeric and ignores it if it's not by moving the pointer by one step.
# These steps are counted in the total number of visit of the function

# In conclusion, we can say that the function has running time 
# linear in n, that is O(n), with n is the number of the characters of the string 
# (the size of the string)

# space complexity: O(1)
# no additional storage was used


