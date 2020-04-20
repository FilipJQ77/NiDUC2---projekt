# używanie innych plików - po prostu import nazwa_pliku
# import random
# import time
import data
import hamming

# for i in range(4, 18):
lista1 = [1, 1, 0, 1]  # data.generate_random_data(i)
data.print_data(lista1)
lista1 = hamming.encode_hamming(lista1)
data.print_data(lista1)
lista2 = [0, 0, 1, 0, 1, 0, 1, 1] # [1, 0, 1, 0, 1, 0, 1, 0] # correct
lista1 = hamming.decode_hamming(lista2)
data.print_data(lista1)
