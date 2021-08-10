# Python3 code to demonstrate working of
# Convert numeric words to numbers
# Using word2number
from word2number import w2n

# initializing string
test_str = "three million"

# printing original string
print("The original string is : " + test_str)

# Convert numeric words to numbers
# Using word2number
res = w2n.word_to_num(test_str)
print(type(res))

# printing result
print("The string after performing replace : " + str(res))
