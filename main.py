# używanie innych plików - po prostu import nazwa_pliku
# import random
# import time
import data

lista1 = data.generate_random_data(4)
data.print_data(lista1)
lista1 = data.encode_data(lista1, "R")
data.print_data(lista1)
lista1 = data.distort_bits(lista1, 90)
data.print_data(lista1)
lista1 = data.decode_data(lista1, "R")
data.print_data(lista1)
