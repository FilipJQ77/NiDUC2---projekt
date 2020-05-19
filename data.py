import math
import random
import statistics
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import csv
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


def gauss_function(x, a, mu, sigma):
    return a * math.e ** ((-1 / 2) * (((x - mu) / sigma) ** 2))


# generates given amount of random data
def generate_random_data(data_amount: int) -> list:
    bits = []
    for i in range(0, data_amount):
        bits.append(random.randint(0, 1))
    return bits


def analyse_data(filename: str):
    results = import_csv(filename)
    analyse(results)


def analyse(results: dict):
    for desc, result_list in results.items():  # desc = key, result_list = item
        mode = statistics.mode(result_list)
        average = statistics.mean(result_list)
        print(f"{desc}: Average = {average}")
        standard_deviation = statistics.stdev(result_list)
        print(f"{desc}: Standard deviation = {standard_deviation}")
        quartiles = statistics.quantiles(result_list, method='inclusive')
        print(f"{desc}: Quartiles = {quartiles}")
        iqr = quartiles[2] - quartiles[0]
        q0 = quartiles[0] - 1.5 * iqr
        q4 = quartiles[2] + 1.5 * iqr
        if standard_deviation:
            skewness_mode = (average - mode) / standard_deviation
            skewness_median = 3 * (average - quartiles[1]) / standard_deviation
            print(f"{desc}: Pearson skewness (mode) = {skewness_mode}")
            print(f"{desc}: Pearson skewness (median) = {skewness_median}")
        else:
            print(f"Skewness = 0")
        plt.boxplot([q0, quartiles[0], quartiles[1], quartiles[2], q4])  # boxplot
        plt.waitforbuttonpress()
        plt.clf()
        # counts, bins, bars = plt.hist(result_list, bins=np.arange(min(result_list), max(result_list) + 1, 1))  # histogram
        counts, bins, bars = plt.hist(result_list, bins=20)  # histogram
        # todo osie wykresu, boxplot nad histogramem
        plt.waitforbuttonpress()
        x_data = []
        for i in range(len(bins) - 1):
            x_data.append((bins[i] + bins[i + 1]) / 2)
        y_data = counts
        params, params_cov = opt.curve_fit(gauss_function, x_data, y_data, p0=[max(y_data), quartiles[1], iqr / 1.3490])
        print(f"Gauss parameters: {params}")
        plt.plot(x_data, gauss_function(x_data, params[0], params[1], params[2]), label="Fitted function")
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


def export_csv(filename: str, results: dict):
    with open(filename, 'a', newline='') as file:
        csvwriter = csv.DictWriter(file, results.keys())
        csvwriter.writerow(results)


def import_csv(filename: str) -> dict:
    data_to_analyse = {correct: [], fixed: [], repeat: [], wrong: []}
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file, fieldnames=data_to_analyse.keys())
        for row in csvreader:
            data_to_analyse[correct].append(int(row[correct]))
            data_to_analyse[fixed].append(int(row[fixed]))
            data_to_analyse[repeat].append(int(row[repeat]))
            data_to_analyse[wrong].append(int(row[wrong]))
    return data_to_analyse


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
        while True:
            decoded_data.append(decode_data(sent_data[i], code_type))
            if (decoded_data[i])[-1] == repeat_message:
                data_results[repeat] += 1
                decoded_data.pop()
                sent_data[i] = distort_bits(encoded_data[i], probability)
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
    filename = f"{code_type}_{len(bits)}_{block_size}_{probability}.csv"
    export_csv(filename, data_results)
    return data_results
