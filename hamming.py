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
                # todo ten if jest po to że jeśli mamy niepełny kod hamminga to nie wiemy kiedy jest koniec danych
                if i <= bits_amount:
                    summ += bits[i - 1]
                    i += 1
            i += index
        bits[index - 1] = summ % 2
        index *= 2
    return bits


# todo dodanie jeszcze jednego bitu parzystości aby wykrywać błędy 2 bitów,
#  ogarnąć co sie dzieje gdy indeks złego bitu jest poza zakresem listy
def decode_hamming(bits: list) -> list:
    bits_amount = len(bits)
    index = 1
    wrong_bit_index = 0
    while index <= bits_amount:
        i = index
        summ = 0
        while i <= bits_amount:
            for j in range(index):
                # todo ten if jest po to że jeśli mamy niepełny kod hamminga to nie wiemy kiedy jest koniec danych
                if i <= bits_amount:
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
    index = 1
    new_bits = []
    for i in range(bits_amount):
        if i + 1 == index:
            index *= 2
        else:
            new_bits.append(bits[i])
    return new_bits
