import numpy as np

divisor = [1, 0, 0, 1, 0, 1]
len_divisor = len(divisor)


def encode_crc(bits: list) -> list:
    new_bits = list.copy(bits)
    bits_temp = list.copy(bits)
    for i in range(len_divisor - 1):
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
    bits_temp = list.copy(bits)
    bits_amount = len(bits)
    for i in range(bits_amount - len_divisor + 1):
        if bits_temp[i] == 1:
            for j in range(len_divisor):
                bits_temp[i + j] = int(np.logical_xor(bits_temp[i + j], divisor[j]))
    summ = 0
    for i in range(len_divisor):
        summ += bits_temp[bits_amount - 1 - i]
    print(bits_temp)
    if summ == 0:
        return bits[:-(len_divisor - 1)]
    elif summ == 1:
        new_bits = bits[:-(len_divisor - 1)]
        new_bits.append("F")
        return new_bits
    else:
        return repair_crc(bits)


def repair_crc(broken: list) -> list:
    broken_1 = list.copy(broken)
    broken_2 = list.copy(broken)
    len_broken = len(broken)
    rotations = 0
    while rotations < len_broken - 1:
        broken_1 = broken_1[1:] + broken_1[:1]
        rotations += 1
        for i in range(len_broken - len_divisor + 1):
            if broken_1[i] == 1:
                for j in range(len_divisor):
                    broken_2[i + j] = int(np.logical_xor(broken_1[i + j], divisor[j]))
        print(broken_2, rotations)
        test = sum(broken_2)
        if test == 1:
            for i in range(len_broken):
                broken_1[i] += broken_2[i]
            broken_1 = broken_1[-rotations:] + broken_1[:-rotations]
            return broken_1
    return ["R"]
