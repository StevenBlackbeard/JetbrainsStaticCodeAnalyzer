import re

string = input()
# string = "$30"
regex = r'\$\d+'
match = re.match(regex, string)
if bool(match):
    print('Amount found:', match.group())
else:
    print('No match!')