import re

word = input()
# your code here
# word = "theft" # False
# word = "the" # True
# word = "tthe" # False
template = r'the$'
print(bool(re.match(template, word)))
