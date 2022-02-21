# s1 = input()
# s2 = input()

def combine(s1, s2):
    list_out = []
    for e in zip(s1, s2):
        list_out.append("".join(e))
    print("".join(list_out))

combine(input(), input())