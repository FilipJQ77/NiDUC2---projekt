def encode_repetition(bits: list) -> list:
    """Encodes a given list of bits with a repetition code (repeating each bit 4 times)."""
    new_bits = []
    for bit in bits:
        for i in range(4):
            new_bits.append(bit)
    return new_bits


def decode_repetition(bits: list) -> list:
    """Decodes a given list of bits with a repetition code."""
    index = 1
    summ = 0
    is_fixed = ""
    new_bits = []
    for bit in bits:
        summ += bit
        if index == 4:
            index = 0
            if summ > 2:
                new_bits.append(1)
                if summ == 3:
                    is_fixed = "F"
            elif summ < 2:
                new_bits.append(0)
                if summ == 1:
                    is_fixed = "F"
            else:
                return ["R"]
            summ = 0
        index += 1
    if is_fixed:
        new_bits.append(is_fixed)
    return new_bits
