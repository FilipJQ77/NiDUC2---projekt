import numpy as np


# todo zrobić Hamminga na dowolnej ilości bitów informacji
def encode_hamming(bits: list) -> list:
    datamat = np.array(bits)
    data_matrix = np.array([(bits[0]), (bits[1]), (bits[2]), (bits[3])])
    # codeword = np.multiply(generator_matrix, data_matrix)
    # print(codeword)
    # bits = list(codeword)
    # return bits


# todo decodes a given list of 7 bits of Hamming (7,4) code into 4 bits of data if possible, otherwise returns None
def decode_hamming(bits: list) -> list:
    return None
