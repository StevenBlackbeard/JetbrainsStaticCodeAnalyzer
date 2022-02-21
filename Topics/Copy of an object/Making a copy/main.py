import copy

def my_copy(obj, copy_mode):
    if copy_mode == "deep copy":
        out = copy.deepcopy(obj)
    else:
        out = copy.copy(obj)
    return out
