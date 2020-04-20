import random
# import time
import data
import hamming

# for i in range(4, 18):
lista1 = data.generate_random_data(11)
data.print_data(lista1)
lista1 = hamming.encode_hamming(lista1)
data.print_data(lista1)
what_to_test = "F"  # todo albo "R", w zależności co testujesz
lista_size = len(lista1) - 1
if what_to_test == "F":
    i1 = random.randint(0, lista_size)
    lista1[i1] = data.distort_bit(lista1[i1], 0)
else:
    i1 = random.randint(0, lista_size)
    lista1[i1] = data.distort_bit(lista1[i1], 0)
    i2 = random.randint(0, lista_size)
    while i1 == i2:
        i2 = random.randint(0, lista_size)
    lista1[i2] = data.distort_bit(lista1[i2], 0)
data.print_data(lista1)
lista1 = hamming.decode_hamming(lista1)
data.print_data(lista1)
