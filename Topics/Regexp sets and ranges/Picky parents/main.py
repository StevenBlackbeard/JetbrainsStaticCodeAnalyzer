import re

# your code here
str_in = input()
# str_in = 'Butterfly'
template = '[B-N][aeiou]'
if bool(re.match(template, str_in)):
    print("Suitable!")