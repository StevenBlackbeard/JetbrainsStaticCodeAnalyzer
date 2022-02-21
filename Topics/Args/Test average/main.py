# def average_mark(*marks):
#     total = 0
#     count = 0
#     for n in marks:
#         total += n
#         count += 1
#     return round(total / count, 1)

def average_mark(*args):
    return round(sum(args) / len(args), 1)