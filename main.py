import sys

import data
import random

crc_code = "C"
hamming_code = "H"
repetition_code = "R"


# interface
def export():
    while True:
        code_type = input("Podaj typ kodu (Hamming - H, CRC - C, Powtorzeniowy - R): ")
        code_type = code_type.upper()
        if code_type == "":
            break
        bits_amount = int(input("Podaj ilość bitów do wygenerowania: "))
        block_size = int(input("Podaj ilość bitów w pakiecie: "))
        prob = float(input("Podaj prawdopodobieństwo przekłamania bitu: "))
        attempts = int(input("Ile prób wykonać?: "))
        for i in range(attempts):
            listt = data.generate_random_data(bits_amount)
            data.sending_data(listt, block_size, code_type, prob)


def analyse():
    while True:
        code_type = input("Podaj typ kodu (Hamming - H, CRC - C, Powtorzeniowy - R, nic - wyjście): ")
        code_type = code_type.upper()
        if code_type == "":
            break
        bits_amount = int(input("Podaj ilość bitów w wiadomosci: "))
        block_size = int(input("Podaj ilość bitów w pakiecie: "))
        prob = float(input("Podaj prawdopodobieństwo przekłamania bitu: "))
        filename = f"{code_type}_{bits_amount}_{block_size}_{prob}.csv"
        data.analyse_data(filename)


def menu():
    answer = True
    while answer:
        print("1. Eksport\n2. Analiza\n0. Wyjście")
        answer = input()
        if answer == "1":
            export()
        elif answer == "2":
            analyse()
        elif answer == "0":
            answer = None
        else:
            print("Niepoprawna opcja")


menu()


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
