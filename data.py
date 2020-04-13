import random
import numpy as np

generator_matrix = np.array(
    ((1, 1, 0, 1), (1, 0, 1, 1), (1, 0, 0, 0), (0, 1, 1, 1), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))

parity_check_matrix = np.array(((1, 0, 1, 0, 1, 0, 1), (0, 1, 1, 0, 0, 1, 1), (0, 0, 0, 1, 1, 1, 1)))


# generates random bits of data (true or false) todo: albo t/f albo 0/1, co lepsze?
def generate_random_data_bool(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        random_number = random.randint(0, 1)
        if random_number == 0:
            bits.append(False)
        else:
            bits.append(True)
    return bits


# prints data generated with generate_random_data_bool
def print_data_bool(bits: list):
    print(f"Data of a list with id:{id(bits)}: [", end='')
    for boolean in bits:
        if boolean:
            print(1, end='')
            pass
        else:
            print(0, end='')
            pass
    print("]")


# todo: na razie będzie robione na liczbach, potem można to najwyżej zoptymalizować
def generate_random_data(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        bits.append(random.randint(0, 1))
    return bits


# todo zaburzanie sygnału
def distort_bits(bits: list) -> list:
    pass


# todo: przekazujemy ciąg bitów, a funkcja podzieli je na 4 bitowe fragmenty, zwraca listę list(?)
def separate_data(bits: list) -> list:
    pass


# encodes given list of 4 bits into a Hamming (7,4) code todo
def encode_hamming(bits: list) -> list:
    datamat = np.array(bits)
    data_matrix = np.array([(bits[0]), (bits[1]), (bits[2]), (bits[3])])
    codeword = np.multiply(generator_matrix, data_matrix)
    print(codeword)
    # bits = list(codeword)
    # return bits


# decodes given list of 7 bits of Hamming (7,4) code into 4 bits of data if possible, otherwise returns None todo
def decode_hamming(bits: list) -> list:
    return None


# expects 4 bits
def encode_parity(bits: list) -> list:
    i = 0
    for bit in bits:
        i += bit
    bits.append(i % 2)
    return bits


# expects 5 bits
def decode_parity(bits: list) -> list:
    i = 0
    for bit in bits:
        i += bit
    i -= bits[-1]
    i = i % 2
    if i == bits[-1]:
        bits.pop()
        return bits
    else:
        return None


# expects 4 bits, todo powtarzanie bitu razy 3, czy może 4?
def encode_repeat(bits: list) -> list:
    pass


# expects
def decode_repeat(bits: list) -> list:
    pass


# prints data generated with generate_random_data_bool
def print_data(bits: list):
    print(f"Data of a list with id:{id(bits)}: [", end='')
    for bit in bits:
        print(bit, end='')
    print("]")
