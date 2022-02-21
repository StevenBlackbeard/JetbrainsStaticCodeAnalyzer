# def tallest_people(lst):
#     # lst = ("Jackie 176", "Wilson 185", "Saersha 165", "Roman 185", "Abram 169")
#     lst = [n.split(" ") for n in lst]
#     lst = [[n[0], int(n[1])] for n in lst]
#     max_val = max(n[1] for n in lst)
#     lst = [n for n in lst if n[1] == max_val]
#     lst.sort(key=lambda x: x[0])
#     lst = [[n[0], str(n[1])] for n in lst]
#     lst = [" : ".join(n) for n in lst]
#     for i in lst:
#         print(i)

def tallest_people(**kwargs):
    max_val = max(kwargs.values())
    for key, value in sorted(kwargs.items()):
        if value == max_val:
            print(key, ":", value)

# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)

# other 1
# def tallest_people(**kwargs):
#     print("\n".join(sorted(f"{i} : {j}" for i, j in kwargs.items() if j == max(kwargs.values()))))
