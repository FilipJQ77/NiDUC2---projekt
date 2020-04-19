import random
import numpy as np
import hamming


# reshape
# binary symmetric channel
# 3 algorytmy
# różna ilość bitów w pakiecie
# kod bch
# kod crc

# generates given amount of random data
def generate_random_data(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        bits.append(random.randint(0, 1))
    return bits


# prints data generated with generate_random_data
def print_data(bits: list):
    print(f"Data of a list with id: {id(bits)}: [", end='')
    for bit in bits:
        print(bit, end='')
    print("]")


# separates data into blocks of size n, returns a list of lists, where each inside list is a block of data
def separate_data(bits: list, n: int) -> list:
    i = 0
    complete_data = []
    block_of_data = []
    for bit in bits:
        i += 1
        block_of_data.append(bit)
        if i == n:
            i = 0
            complete_data.append(block_of_data)
            block_of_data = []

    # if we still have some data which wasn't added, we fill it with 0s until it has a size of n
    if block_of_data:
        length = len(block_of_data)
        for i in range(length, n):
            block_of_data.append(0)
        complete_data.append(block_of_data)
    return complete_data


# basic distortion of a single bit, probability is in range [0,100]
def distort_bit(bit: int, probability: int) -> int:
    rand = random.randint(0, 100)
    if rand >= probability:
        if bit == 0:
            bit = 1
        else:
            bit = 0
    return bit


# basic distortion of data, probability is in range [0,100] todo pomyśleć nad innymi implementacjami
def distort_bits(bits: list, probability: int) -> list:
    size = len(bits)
    for i in range(0, size):
        bits[i] = distort_bit(bits[i], probability)
    return bits


# todo temporary
def encode_bch(bits: list) -> list:
    return bits


# todo temporary
def encode_crc(bits: list) -> list:
    return bits


# todo temporary
def decode_bch(bits: list) -> list:
    return bits


# todo temporary
def decode_crc(bits: list) -> list:
    return bits


# encodes a block of data with a given type of code
def encode_data(block_of_data: list, code_type: str) -> list:
    if code_type == "B":
        block_of_data = encode_bch(block_of_data)
    elif code_type == "C":
        block_of_data = encode_crc(block_of_data)
    elif code_type == "H":
        block_of_data = hamming.encode_hamming(block_of_data)
    return block_of_data


def decode_data(block_of_data: list, code_type: str) -> list:
    if code_type == "B":
        block_of_data = decode_bch(block_of_data)
        pass
    elif code_type == "C":
        block_of_data = decode_crc(block_of_data)
        pass
    elif code_type == "H":
        block_of_data = hamming.decode_hamming(block_of_data)
        pass
    return block_of_data


# todo symulacja przesyłania danych, code_type to typ kodu (crc, bch itp)
# todo zwraca co się stało tzn. czy wiadomość odebrana była poprawna, czy wykryto błąd, naprawiono błąd itp.
def sending_data(bits: list, block_size: int, code_type: str, probabilty: int) -> str:
    separated_data = separate_data(bits, block_size)
    data_size = len(separated_data)
    sent_data = []
    for block in separated_data:
        sent_data.append(encode_data(block, code_type))
    for i in range(data_size):
        sent_data[i] = distort_bits(sent_data[i], probabilty)
    decoded_data = []
    block_results = ["" for x in range(data_size)]
    for i in range(data_size):
        while True:
            decoded_data.append(decode_data(sent_data[i], code_type))
            # todo ---> każdy sposób dekodowania musi dodawać na koniec info co się stało,
            #  jeśli ostatnim elementem bloku jest "F" (fixed) to wiemy że udało się naprawić informację,
            #  jeśli "R" (repeat) to musimy wysłać informację jeszcze raz,
            #  jeśli nie ma ani F ani R, to informacja według dekodera jest poprawna
            if (decoded_data[-1])[-1] == "F":
                block_results[i] += "F"
                decoded_data[-1].pop()
                break
            elif (decoded_data[-1])[-1] == "R":
                block_results[i] += "R"
                decoded_data[-1].pop()
            else:
                block_results[i] += "C"  # correct
                break
    len(block_results)  # de facto liczba wysłań bloków
    data_results = {"Correct": 0, "Fixed correctly": 0, "Fixed wrongly": 0, "Didn't detect error": 0}
    for i in range(data_size):
        if separated_data[i] == decoded_data[i]:
            data_results["Correct"] += 1
            # todo wtedy jest correct itd dla każdego przypadku
            pass

    return data_results


# todo Aga to jest twój kod do edycji
# encodes a given list of 4 bits into a list of 12 bits, where each bit is tripled
def encode_repeat(bits: list) -> list:
    new_bits = []
    for bit in bits:
        for i in range(0, 3):
            new_bits.append(bit)
    return new_bits


# decodes a given list of 12 bits into a list of 4 bits
def decode_repeat(bits: list) -> list:
    index = 1
    summ = 0
    new_bits = []
    for bit in bits:
        summ += bit
        if index == 3:
            index = 0
            if summ > 1:
                new_bits.append(1)
            else:
                new_bits.append(0)
            summ = 0
        index += 1
    return new_bits
