def heading(char_in, length=1):
    length = max(min(length, 6), 1)
    return f"{'#' * length} {char_in}"
    # if length < 1:
    #     length = 1
    # elif length > 6:
    #     length = 6
    # else:
    #     length = length
    # return f'{"#" * length} {char_in}'


# def heading(char_in, length=None):
#     if length is None:
#         length = 1
#
#     if length < 1:
#         length_out = 1
#     elif length > 6:
#         length_out = 6
#     else:
#         length_out = length
#     return f'{"#" * length_out} {char_in}'