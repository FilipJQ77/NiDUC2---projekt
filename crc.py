import numpy as np

divisor = [1, 0, 1, 1]


def encode_crc(bits: list) -> list:
    new_bits = list.copy(bits)
    bits_temp = []
    for bit in new_bits:
        bits_temp.append(bit)
    for i in range(len(divisor) - 1):
        bits_temp.append(0)
    bits_amount = len(new_bits)
    for i in range(bits_amount):
        if bits_temp[i] == 1:
            for j in range(len(divisor)):
                bits_temp[i + j] = int(np.logical_xor(bits_temp[i + j], divisor[j]))
    for i in range(len(divisor) - 1):
        new_bits.append(bits_temp[bits_amount + i])
    return new_bits


def decode_crc(bits: list) -> list:
    new_bits = list.copy(bits)
    bits_temp = []
    for bit in new_bits:
        bits_temp.append(bit)
    bits_amount = len(new_bits)
    for i in range(bits_amount - len(divisor) + 1):
        if bits_temp[i] == 1:
            for j in range(len(divisor)):
                bits_temp[i + j] = int(np.logical_xor(bits_temp[i + j], divisor[j]))
    summ = 0
    for i in range(len(divisor)):
        summ += bits_temp[bits_amount - 1 - i]
    for i in range(len(divisor) - 1):
        new_bits.pop(-1)
    if summ != 0:
        return ["R"]
    return new_bits
