import re

# define regex template
template = '[0-9a-fA-F][0-9a-fA-F]?' # or template = '[a-fA-F0-9]{1,2}'


# Let's compose a regexp that would match strings containing one- or two-digit hexadecimal numbers.
# A "digit" of a hexadecimal number can be either a digit from 0 to 9 (including 9), or
# a small or capital letter from A to F (including F). The examples of hexadecimal numbers we
# want to match:
#
# AA
# 1
# 6f
# d9
# 3E
# c1
# 9