import sys

import data
import random

# crc_code = "C"
# hamming_code = "H"
# repetition_code = "R"

#
# lista1 = data.generate_random_data(60)
#
# # todo zmiana jednego bitu
# # i1 = random.randint(0, lista_size)
# # lista1[i1] = data.distort_bit(lista1[i1], 0)
#
# # todo zmiana dwóch bitów
# # i1 = random.randint(0, lista_size)
# # lista1[i1] = data.distort_bit(lista1[i1], 0)
# # i2 = random.randint(0, lista_size)
# # while i1 == i2:
# #    i2 = random.randint(0, lista_size)
# # lista1[i2] = data.distort_bit(lista1[i2], 0)
#
# # dict1 = data.sending_data(lista1, 6, "H", 0.03)
# # dict2 = data.sending_data(lista1, 6, "H", 0.03)
# # print(dict1)
# # print(dict2)
#
correct = "Correct"
fixed = "Fixed"
repeat = "Repeat"
wrong = "Wrong"


# dicto = {correct: [9, 8, 7, 6, 0, 9, 9, 8],
#          fixed: [0, 1, 3, 3, 7, 0, 1, 1],
#          repeat: [0, 1, 3, 2, 2, 2, 4, 5],
#          wrong: [1, 1, 0, 1, 3, 1, 0, 1]}
# dicto = {correct: []}
# for i in range(100000):
#     x = int(random.triangular(0, 1000, 750))
#     dicto[correct].append(x)
# data.analyse(dicto)

# for i in range(10):
#     lista = data.generate_random_data(400)
#     data.sending_data(lista, 4, hamming_code, 0.01)

# data.analyse_data("H_400_4_0.01.csv")


# INTERFEJS
def export():
    while True:
        code_type = input("Podaj typ kodu (Hamming - H, CRC - C, Powtorzeniowy - R): ")
        if code_type == "":  # wyjście to po prostu nie podanie niczego do typu kodu
            break
        bits_amount = int(input("Podaj ilość bitów do wygenerowania: "))
        block_size = int(input("Podaj ilość bitów w pakiecie: "))
        prob = float(input("Podaj prawdopodobieństwo przekłamania bitu: "))
        ile_razy = int(input("Ile prób wykonać?: "))
        for i in range(ile_razy):
            list = data.generate_random_data(bits_amount)
            data.sending_data(list, block_size, code_type, prob)


def analyse():
    while True:
        code_type = input("Podaj typ kodu (Hamming - H, CRC - C, Powtorzeniowy - R): ")
        if code_type == "":  # wyjście to po prostu nie podanie niczego do typu kodu
            break
        bits_amount = int(input("Podaj ilość bitów w wiadomosci: "))
        block_size = int(input("Podaj ilość bitów w pakiecie: "))
        prob = float(input("Podaj prawdopodobieństwo przekłamania bitu: "))
        filename = f"{code_type}_{bits_amount}_{block_size}_{prob}.csv"
        data.analyse_data(filename)


ans = True
while ans:
    print("""
    1.Export
    2.Analyse
    0.Exit
    """)
    ans = input()
    if ans == "1":
        export()
    elif ans == "2":
        analyse()
    elif ans == "0":
        ans = None
    else:
        print("\n Not Valid Choice Try again")
