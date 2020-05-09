import random
import statistics
import matplotlib.pyplot as plt
import crc
import hamming
import repetition

crc_code = "C"
hamming_code = "H"
repetition_code = "R"
fixed_message = "F"
repeat_message = "R"
correct = "Correct"
fixed = "Fixed"
repeat = "Repeat"
wrong = "Wrong"
amount = "Amount"


# generates given amount of random data
def generate_random_data(data_amount: int) -> list:
    bits = []
    for i in range(0, data_amount):
        bits.append(random.randint(0, 1))
    return bits


def export_csv(filename: str, results: dict):
    pass  # todo


def import_csv(filename: str) -> dict:
    dictt = {correct: [], fixed: [], repeat: [], wrong: []}
    # todo bierzesz linijke, appendujesz do odpowiedniej listy odpowiednie wartosci
    # dictt[correct].append(sczytana wartosc) etc
    return dictt


def analyse_data(filename: str):
    results = import_csv(filename)
    # tu bedzie kod z metody analyse ktora jest teraz placeholderem


def analyse(results: dict):
    for desc, result in results.items():  # desc = key, result = item
        mode = statistics.mode(result)
        average = statistics.mean(result)
        print(f"{desc}: Average = {average}")
        standard_deviation = statistics.stdev(result)
        print(f"{desc}: Standard deviation = {standard_deviation}")
        quartiles = statistics.quantiles(result, method='inclusive')
        print(f"{desc}: Quartiles = {quartiles}")
        iqr = quartiles[2] - quartiles[0]
        q0 = quartiles[0] - 1.5 * iqr
        q4 = quartiles[2] + 1.5 * iqr
        skewness_mode = (average - mode) / standard_deviation
        skewness_median = 3 * (average - quartiles[1]) / standard_deviation
        print(f"{desc}: Pearson skewness (mode) = {skewness_mode}")
        print(f"{desc}: Pearson skewness (median) = {skewness_median}")
        plt.boxplot([q0, quartiles[0], quartiles[1], quartiles[2], q4])  # boxplot
        plt.waitforbuttonpress()  # todo raczej mozna lepiej
        plt.clf()
        plt.hist(result, bins=100)  # histogram
        plt.waitforbuttonpress()
        plt.clf()


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


# basic distortion of data, probability (of distorting a bit) is in range [0, 1]
def distort_bit(bit: int, probability: float) -> int:
    rand = random.uniform(0, 1)
    if rand < probability:
        if bit == 0:
            bit = 1
        else:
            bit = 0
    return bit


# basic distortion of data, probability (of distorting a bit) is in range [0, 1]
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
    data_results = {correct: 0, fixed: 0, repeat: 0, wrong: 0}
    for i in range(data_size):
        print(f"Decode {i + 1}")
        while True:
            decoded_data.append(decode_data(sent_data[i], code_type))
            if (decoded_data[i])[-1] == repeat_message:
                data_results[repeat] += 1
                decoded_data.pop()
                sent_data[i] = distort_bits(encoded_data[i], probability)
                print(f"Repeat {i + 1}")
            else:
                break
    for i in range(data_size):
        is_fixed = False
        if decoded_data[i][-1] == fixed_message:
            is_fixed = True
            decoded_data[i].pop()
        if decoded_data[i] == separated_data[i]:
            if is_fixed:
                data_results[fixed] += 1
            else:
                data_results[correct] += 1
        else:
            data_results[wrong] += 1
    # todo parametry symulacji jako nazwa .csv
    # np filename=block_size+probabilty etc
    export_csv()
    return data_results
