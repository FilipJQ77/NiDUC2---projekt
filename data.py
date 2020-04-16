import random
import numpy as np


# reshape
# binary symmetric channel
# 3 algorytmy
# różna ilość bitów w pakiecie
# kod bch
# kod crc


# deprecated? generates random bits of data (true or false) todo: albo t/f albo 0/1, co lepsze?
def generate_random_data_bool(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        random_number = random.randint(0, 1)
        if random_number == 0:
            bits.append(False)
        else:
            bits.append(True)
    return bits


# deprecated? prints data generated with generate_random_data_bool
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

def cos():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

# generates given amount of random data
def generate_random_data(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        bits.append(random.randint(0, 1))
    return bits


# separates data into blocks of size n, returns a list of lists, where each list is a block of data
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


# todo podstawowa metoda kodowania
def encode_data(block_of_data: list, code_type: str) -> list:
    if code_type == "B":
        # kodowanie bch
        # coś w stylu block_of_data = encode_bch(block_of_data)
        pass
    elif code_type == "C":
        # kodowanie crc, jw
        pass
    elif code_type == "H":
        # kodowanie Hamminga, jw
        pass
    return block_of_data


# TODO!!! ---> dekodowanie ma działać podobnie jak poniższe
#  dekodowania bitu parzystości tzn: jeśli coś jest nie tak, trzeba dać jakiś sygnał, np. zwrócenie none czy coś,
#  i pomyśleć nad sposobem przekazywania listy danych oraz tego co się stało podczas dekodowania (3 możliwości:
#  1 - udało się zdekodować, 2 - był błąd, ale naprawiony, 3 - błąd którego nie dało się naprawić)
def decode_data(block_of_data: list, code_type: str) -> list:
    if code_type == "B":
        # dekodowanie bch
        pass
    elif code_type == "C":
        # dekodowanie crc, jw
        pass
    elif code_type == "H":
        # dekodowanie Hamminga, jw
        pass
    return block_of_data


# todo symulacja przesyłania danych, code_type to typ kodu (crc, bch itp)
# todo zwraca co się stało tzn. czy wiadomość odebrana była poprawna, czy wykryto błąd, naprawiono błąd itp.
def sending_data(bits: list, block_size: int, code_type: str, probabilty: int) -> str:
    separated_data = separate_data(bits, block_size)
    encoded_data = []
    for block in separated_data:
        encoded_data.append(encode_data(block, code_type))
    # todo szkic, nie do końca poprawny, chyba bedzie lepiej zrobic osobna metode do przesylania tylko jednego bloku
    for block in encoded_data:
        block = distort_bits(block, probabilty)
    for block in encoded_data:
        block = decode_data(block, code_type)
        if block is None:
            # try again
            pass
    return  # 4 możliwości (1 - poprawna wiadomość, 2 - błąd, ale naprawiony, 3 błąd wykryty, ponowne przesłanie (ile
    # razy trzeba było przesyłać?), 4 - niepoprawna wiadomość, nie wykryto błędu) i np. zliczanie ile razy co sie stalo


# encodes a given list of 4 bits into a list of 5 bits with a parity bit
def encode_parity(bits: list) -> list:
    i = 0
    for bit in bits:
        i += bit
    bits.append(i % 2)
    return bits


# "decodes" a given list of 5 bits with a parity bit into a list of 4 bits of data, if the parity bit is correct
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


# prints data generated with generate_random_data
def print_data(bits: list):
    print(f"Data of a list with id: {id(bits)}: [", end='')
    for bit in bits:
        print(bit, end='')
    print("]")
