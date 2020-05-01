import random
# import time
import data

# for i in range(4, 18):
# lista1 = data.generate_random_data(11)
# data.print_data(lista1)
# lista1 = data.encode_data(lista1, "H")
# data.print_data(lista1)
# what_to_test = "R"  # todo albo "R", w zależności co testujesz
# lista_size = len(lista1) - 1
# if what_to_test == "F":
#     i1 = random.randint(0, lista_size)
#     lista1[i1] = data.distort_bit(lista1[i1], 0)
# else:
#     i1 = random.randint(0, lista_size)
#     lista1[i1] = data.distort_bit(lista1[i1], 0)
#     i2 = random.randint(0, lista_size)
#     while i1 == i2:
#         i2 = random.randint(0, lista_size)
#     lista1[i2] = data.distort_bit(lista1[i2], 0)
# data.print_data(lista1)
# lista1 = data.decode_data(lista1, "H")
# data.print_data(lista1)

lista1 = data.generate_random_data(100)
dictt = data.sending_data(lista1, 5, "C", 0.01)
print(dictt)
