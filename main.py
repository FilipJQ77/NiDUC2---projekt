import random
# import time
import data

lista1 = data.generate_random_data(60)
lista1 = data.encode_data(lista1, "C")

# todo zmiana jednego bitu
# i1 = random.randint(0, lista_size)
# lista1[i1] = data.distort_bit(lista1[i1], 0)

# todo zmiana dwóch bitów
# i1 = random.randint(0, lista_size)
# lista1[i1] = data.distort_bit(lista1[i1], 0)
# i2 = random.randint(0, lista_size)
# while i1 == i2:
#    i2 = random.randint(0, lista_size)
# lista1[i2] = data.distort_bit(lista1[i2], 0)

# data.print_data(lista1)
lista1 = data.decode_data(lista1, "C")
data.print_data(lista1)

print(data.encode_data([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1], "C"))

# print(decode_cyclic(encode_cyclic(lista)))

# [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]

print(data.decode_data([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],"C"))

#lista1 = data.generate_random_data(6000)
#dictt = data.sending_data(lista1, 6, "R", 0.01)
#print(dictt)
