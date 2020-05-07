import random
# import time
import data

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
amount = "Amount"
dicto = data_results = {correct: [9, 8, 7, 6], fixed: [0, 1, 3, 3], repeat: [0, 1, 3, 2], wrong: [1, 1, 0, 1], amount: 4}
print(data.analyse(dicto))
