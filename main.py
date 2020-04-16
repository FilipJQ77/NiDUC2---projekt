# używanie innych plików - po prostu import nazwa_pliku
# import random
# import time
import data
import hamming

# lista = data.generate_random_data(10)
# data.print_data_bool(lista)

# lista2 = data.generate_random_data(5)
# data.print_data_bool(lista2)

# lista.append(True)
# data.print_data_bool(lista)
# lista2.remove(True)
# data.print_data_bool(lista2)

# lista = data.generate_random_data(10)
# data.encode_hamming(lista)

# lista = data.generate_random_data(4)
# data.print_data(lista)
# lista = data.encode_parity(lista)
# data.print_data(lista)
# lista = data.decode_parity(lista)
# if lista is not None:
#     data.print_data(lista)
# else:
#     print("oof")

# while True:
#     lista = data.generate_random_data(4)
#     nowa_lista = data.encode_repeat(lista)
#     nowa_lista = data.decode_repeat(nowa_lista)
#     if lista != nowa_lista:
#         print("oof")

lista1 = data.generate_random_data(13)
data.print_data(lista1)
lista2 = data.separate_data(lista1, 3)
print(lista2)
