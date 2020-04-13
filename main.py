# używanie innych plików - po prostu import nazwa_pliku
# import random
# import time
import data

lista = data.generate_random_data(10)
data.print_data(lista)

lista2 = data.generate_random_data(5)
data.print_data(lista2)

lista.append(True)
data.print_data(lista)
lista2.remove(True)
data.print_data(lista2)