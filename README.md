## Explanation Video
I've recorded a 11-minute video for you to have a better understanding of my work. Please have a look  
https://www.loom.com/share/4b44e46a8a7849d4a1b24d9c13d4b2c0?sid=45cc0cf8-18cf-4b51-855a-0f107a3f7955
 
## PROBLEM 1
__Palindrome String DEFINITION:__  
A string is a palindrome if the string read from left to right
is equal to the string read from right to left, IGNORING the 
difference between uppercase and lowercase letter, and EXCLUDE
all non-alphanumeric characters

__APPROACH:__  
We'll be using two pointers, each starts at each end of the string
At each iteration, the pointers move towards the opposite direction
until they meet at the middle of the string

At each iteration of the loop, the characters at the two pointers
will be checked if they're alphanumeric or not. If not, the pointer
will be moved one step to the left or right. If the two characters are 
alphanumeric, they will be converted to lowercase before being compared.
In case of equal, move both pointers one step to left and right. In case of 
not equal, the string is not a Palindrome

The loop stops when the "start" pointer is greater than the "end" pointer.  
At this time, we can conclude that the string is a Palindrome

I'm using Python as it is my favourite programing language
for solving Data Structure and Algorithm problems

## PROBLEM 2
__APPROACH:__  
The approach is to use two nested loops to iterate through all elements of the matrix. At each iteration, an element of the matrix will be rotated using the following formular:  
```
rotated[i][j] = input[j][n - 1 - i]
```


## PROBLEM 3

#### Questions I would ask the shop manager:

1. How many customers do you currently have?  
I'm asking this to determine the size of the system and to 
predict whether we'll need scaling in the future

2. Apart from registering the inventory, what do you hope 
to achieve when using the web system? For example: generating reports, user visit statistics.  
I'm asking this to get a general sense of the shop manager's expectations, to find out 
what his problems are so that I can provide him with suggestions on how
the web system can automate his jobs and boost his productivity

3. There's a cool thing I'd like to suggest to you. Would you like 
the web system to be your customer care staff? It could automatically answer 
customer's questions related to your products. The system will take advantage
of AI, ChatGTP in particular.   
I'm asking this because this feature can provide a lot of values to 
the shop manager and reduce his human resource costs