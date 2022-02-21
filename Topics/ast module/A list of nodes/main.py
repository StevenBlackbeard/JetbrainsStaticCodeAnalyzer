# import ast
#
# expression = "(34 + 6) * (23**2 - 7 + 45**2)"
#
# # put your code here
# tree = ast.parse(expression)
# nodes = ast.walk(tree)
# list_out = []
# for n in nodes:
#     list_out.append((n))
# print(len(list_out))

import ast

expression = "(34 + 6) * (23**2 - 7 + 45**2)"

# put your code here
print(len(list(ast.walk(ast.parse(expression)))))