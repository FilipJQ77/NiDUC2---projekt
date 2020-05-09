import data
import random

lista1 = data.generate_random_data(60)

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

# dict1 = data.sending_data(lista1, 6, "H", 0.03)
# dict2 = data.sending_data(lista1, 6, "H", 0.03)
# print(dict1)
# print(dict2)

correct = "Correct"
fixed = "Fixed"
repeat = "Repeat"
wrong = "Wrong"
# dicto = {correct: [9, 8, 7, 6, 0, 9, 9, 8],
#          fixed: [0, 1, 3, 3, 7, 0, 1, 1],
#          repeat: [0, 1, 3, 2, 2, 2, 4, 5],
#          wrong: [1, 1, 0, 1, 3, 1, 0, 1]}
dicto = {correct: []}
for i in range(100000):
    x = int(random.triangular(0, 1000, 750))
    dicto[correct].append(x)
data.analyse(dicto)
