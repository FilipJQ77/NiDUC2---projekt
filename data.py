import random
import crc
import hamming
import repetition

crc_code = "C"
hamming_code = "H"
repetition_code = "R"
fixed_message = "F"
repeat_message = "R"


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
def distort_bit(bit: int, probability: float) -> int:
    rand = random.uniform(0, 1)
    if rand < probability:
        if bit == 0:
            bit = 1
        else:
            bit = 0
    return bit


# basic distortion of data, probability is in range [0,100] todo pomyśleć nad innymi implementacjami
def distort_bits(bits: list, probability: float) -> list:
    size = len(bits)
    for i in range(0, size):
        bits[i] = distort_bit(bits[i], probability)
    return bits


# encodes a block of data with a given type of code
def encode_data(block_of_data: list, code_type: str) -> list:
    if code_type == repetition_code:
        block_of_data = repetition.encode_repetition(block_of_data)
    elif code_type == crc_code:
        block_of_data = crc.encode_crc(block_of_data)
    elif code_type == hamming_code:
        block_of_data = hamming.encode_hamming(block_of_data)
    return block_of_data


def decode_data(block_of_data: list, code_type: str) -> list:
    if code_type == repetition_code:
        block_of_data = repetition.decode_repetition(block_of_data)
        pass
    elif code_type == crc_code:
        block_of_data = crc.decode_crc(block_of_data)
        pass
    elif code_type == hamming_code:
        block_of_data = hamming.decode_hamming(block_of_data)
        pass
    return block_of_data


# todo zwraca co się stało tzn. czy wiadomość odebrana była poprawna, czy wykryto błąd, naprawiono błąd itp.
def sending_data(bits: list, block_size: int, code_type: str, probability: float) -> dict:
    separated_data = separate_data(bits, block_size)
    data_size = len(separated_data)
    encoded_data = []
    for block in separated_data:
        encoded_data.append(encode_data(block, code_type))
    sent_data = list.copy(encoded_data)
    for i in range(data_size):
        sent_data[i] = distort_bits(sent_data[i], probability)
    decoded_data = []
    data_results = {"Correct": 0, "Fixed": 0, "Repeat": 0, "Wrong": 0}
    # todo stringi jako stałe(zmienne)
    # todo data results + parametry jako csv, symulacja monte carlo
    for i in range(data_size):
        print(f"Decode {i+1}")
        while True:
            decoded_data.append(decode_data(sent_data[i], code_type))
            if (decoded_data[i])[-1] == repeat_message:
                data_results["Repeat"] += 1
                decoded_data.pop()
                sent_data[i] = distort_bits(encoded_data[i], probability)
                print(f"Repeat {i}")
            else:
                break
    for i in range(data_size):
        fixed = False
        if decoded_data[i][-1] == fixed_message:
            fixed = True
            decoded_data[i].pop()
        if decoded_data[i] == separated_data[i]:
            if fixed:
                data_results["Fixed"] += 1
            else:
                data_results["Correct"] += 1
        else:
            data_results["Wrong"] += 1
    return data_results
