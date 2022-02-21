# iris = {}
#
# def add_iris(id_n, species, petal_length, petal_width, **kwargs):
#     temp_dict = {id_n: {'species': species,
#         'petal_length': petal_length,
#         'petal_width': petal_width}}
#     iris.update(temp_dict)
#     for key, value in kwargs.items():
#         iris[id_n][key] = value
#
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
# iris

# other 1
iris = {}

def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    temp_dict = {id_n: {'species': species,
                        'petal_length': petal_length,
                        'petal_width': petal_width}}
    iris.update(temp_dict)
    iris[id_n].update(kwargs)  # kwargs create dict already

# other 2
# iris = {}
#
# def add_iris(id_n, species, petal_length, petal_width, **kwargs):
#     iris[id_n] = {'species': species,
#                   'petal_length': petal_length,
#                   'petal_width': petal_width,
#                   **kwargs}
