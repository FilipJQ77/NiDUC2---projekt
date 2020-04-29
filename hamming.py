# encodes given list of bits with a Hamming code
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
                # ten if jest po to że jeśli mamy ucięty kod hamminga to nie wiemy kiedy jest koniec danych
                if i <= bits_amount:
                    summ += bits[i - 1]
                    i += 1
            i += index
        bits[index - 1] = summ % 2
        index *= 2
    # after encoding the information with Hamming code we add an extra parity bit (SECDED)
    summ = 0
    for i in range(bits_amount):
        summ += bits[i]
    bits.append(summ % 2)
    return bits


# decodes given list of bits with a Hamming code
def decode_hamming(bits: list) -> list:
    bits_amount = len(bits)
    index = 1
    wrong_bit_index = 0
    fixed = ""
    while index < bits_amount:
        i = index
        summ = 0
        while i < bits_amount:
            for j in range(index):
                # ten if jest po to że jeśli mamy ucięty kod hamminga to nie wiemy kiedy jest koniec danych
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
        summ = 0
        # checking the additional parity bit
        for i in range(bits_amount - 1):
            summ += bits[i]
        # todo check
        if summ % 2 == bits[-1]:
            fixed = "F"
        else:
            return ["R"]
    index = 1
    new_bits = []
    for i in range(bits_amount - 1):
        if i + 1 == index:
            index *= 2
        else:
            new_bits.append(bits[i])
    if fixed:
        new_bits.append(fixed)
    return new_bits
