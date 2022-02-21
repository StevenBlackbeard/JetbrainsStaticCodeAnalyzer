import re

good_string = 'You learn Python 3?..'
bad_string = 'You learn Python 3?!.'
template = re.escape(good_string)
# template = 'You learn Python 3\?\.\.'
# bool(re.match(template, good_string))
# bool(re.match(template, bad_string))
