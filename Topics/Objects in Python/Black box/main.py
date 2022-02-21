# use the function blackbox(lst) that is already defined
lst = list()
if id(lst) == id(blackbox(lst)):
    print("same")
else:
    print("new")