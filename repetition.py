#
def encode_repetition(bits: list) -> list:
    new_bits = []
    for bit in bits:
        for i in range(4):
            new_bits.append(bit)
    return new_bits


#
def decode_repetition(bits: list) -> list:
    index = 1
    summ = 0
    if_fixed = ""

    new_bits = []
    for bit in bits:
        summ += bit
        if index == 4:
            index = 0
            if summ > 2:
                new_bits.append(1)
                if summ == 3:
                    if_fixed = "F"
            elif summ < 2:
                new_bits.append(0)
                if summ == 1:
                    if_fixed = "F"
            else:
                return ["R"]
            summ = 0
        index += 1
    if if_fixed:
        new_bits.append(if_fixed)
    return new_bits
