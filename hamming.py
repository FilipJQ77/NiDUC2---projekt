import numpy as np
import math


# https://en.wikipedia.org/wiki/Hamming_code#General_algorithm
def encode_hamming(bits: list) -> list:
    bits_amount = len(bits)
    index = 1
    # adding parity bits in correct places to the list
    while index <= bits_amount:
        bits.insert(index - 1, 0)
        bits_amount += 1
        index *= 2
    # algorithm step 5
    index = 1
    while index <= bits_amount:
        i = index
        summ = 0
        while i <= bits_amount:
            for j in range(index):
                # todo ten if jest po to że jeśli mamy ucięty kod hamminga to nie wiemy kiedy jest koniec danych
                if i <= bits_amount:
                    summ += bits[i - 1]
                    i += 1
            i += index
        bits[index - 1] = summ % 2
        index *= 2
    # po zakodowaniu wiadomosci zwyklym hammingiem dodajemy na koniec dodatkowy bit parzystosci (SECDED)
    summ = 0
    for i in range(bits_amount):
        summ += bits[i]
    bits.append(summ % 2)
    return bits


# todo dodanie jeszcze jednego bitu parzystości aby wykrywać błędy 2 bitów, <- zrobione
#  ogarnąć co sie dzieje gdy indeks złego bitu jest poza zakresem listy
#  może być problem z dekodowaniem listy, ponieważ ostatni bit jest dodatkowym bitem parzystości
def decode_hamming(bits: list) -> list:
    bits_amount = len(bits)
    index = 1
    wrong_bit_index = 0
    if_fixed = ""
    while index < bits_amount:
        i = index
        summ = 0
        while i < bits_amount:
            for j in range(index):
                # todo ten if jest po to że jeśli mamy ucięty kod hamminga to nie wiemy kiedy jest koniec danych
                if i < bits_amount:
                    summ += bits[i - 1]
                    i += 1
            i += index
        if summ % 2 != 0:
            wrong_bit_index += index
        index *= 2

    if wrong_bit_index:
        wrong_bit_index -= 1
        if bits[wrong_bit_index]:
            bits[wrong_bit_index] = 0
        else:
            bits[wrong_bit_index] = 1
        # sprawdzamy czy ostatni bit parzystości jest dobry
        summ = 0
        for i in range(bits_amount - 1):
            summ += bits[i]
        if summ % 2 == bits[bits_amount - 1]:
            if_fixed = "F"  # jesli sie zgadza to uznajemy za naprawiony
        else:
            return ["R"]  # jesli sie nie zgadza to zwracamy R

    index = 1
    new_bits = []
    for i in range(bits_amount):
        if i + 1 == index:
            index *= 2
        else:
            new_bits.append(bits[i])
    if if_fixed:
        new_bits.append(if_fixed)  # jesli wiadomosc byla naprawiana dodajemy na koniec F
    return new_bits
