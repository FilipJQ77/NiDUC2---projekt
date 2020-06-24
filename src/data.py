import math
import random
import statistics
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import csv
from src import repetition, crc, hamming

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
    """Gauss function used in curve fitting."""
    return a * math.e ** ((-1 / 2) * (((x - mu) / sigma) ** 2))


def generate_random_data(data_amount: int) -> list:
    """Generates given amount of random bits."""
    bits = []
    for i in range(0, data_amount):
        bits.append(random.randint(0, 1))
    return bits


def analyse_data(filename: str):
    """Analyses sending data test results from given file."""
    results = import_csv(filename)
    analyse(results)


def analyse(results: dict):
    """Analyses sending data test results in form of a dictionary of lists."""
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
        fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True)
        fig.suptitle(f"{desc}: transmissions")
        ax_box.title.set_text("Boxplot")
        ax_hist.title.set_text("Histogram")
        ax_hist.set_xlabel(f"Number of packets sent: {desc}")
        ax_hist.set_ylabel(f"Frequency")
        # boxplot and histogram
        ax_box.boxplot([q0, quartiles[0], quartiles[1], quartiles[2], q4], vert=False)
        counts, bins, bars = ax_hist.hist(result_list, bins=np.arange(min(result_list), max(result_list) + 1, 1))
        # counts, bins, bars = plt.hist(result_list, bins=20)  # histogram
        x_data = []
        for i in range(len(bins) - 1):
            x_data.append((bins[i] + bins[i + 1]) / 2)
        y_data = counts
        params, params_cov = opt.curve_fit(gauss_function, x_data, y_data, p0=[max(y_data), quartiles[1], iqr / 1.349])
        print(f"{desc}: gauss parameters: {params}")
        ax_hist.plot(x_data, gauss_function(x_data, params[0], params[1], params[2]), label="Fitted function")
        plt.waitforbuttonpress()


def print_data(bits: list):
    """Prints data generated with generate_random_data."""
    print(f"Data of a list with id: {id(bits)}: [", end='')
    for bit in bits:
        print(bit, end='')
    print("]")


def separate_data(bits: list, n: int) -> list:
    """Separates data into blocks of size 'n', returns a list of lists, where each internal list is a block of data."""
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
    # if after separating data into blocks we still have some data which wasn't added,
    # we fill it with 0s until it has a size of n
    if block_of_data:
        length = len(block_of_data)
        for i in range(length, n):
            block_of_data.append(0)
        complete_data.append(block_of_data)
    return complete_data


def distort_bit(bit: int, probability: float) -> int:
    """Basic distortion of a bit with probability is in range [0, 1]."""
    rand = random.uniform(0, 1)
    if rand < probability:
        if bit == 0:
            bit = 1
        else:
            bit = 0
    return bit


def distort_bits(bits: list, probability: float) -> list:
    """Basic distortion of data, where each bit can be distorted with a probability in range [0, 1]."""
    for i in range(len(bits)):
        bits[i] = distort_bit(bits[i], probability)
    return bits


def encode_data(block_of_data: list, code_type: str) -> list:
    """Encodes a block of data with a given code type."""
    if code_type == repetition_code:
        block_of_data = repetition.encode_repetition(block_of_data)
    elif code_type == crc_code:
        block_of_data = crc.encode_crc(block_of_data)
    elif code_type == hamming_code:
        block_of_data = hamming.encode_hamming(block_of_data)
    return block_of_data


def decode_data(block_of_data: list, code_type: str) -> list:
    """Decodes a block of data with a given code type."""
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
    """Exports a dictionary of sending data test results to a corresponding csv file."""
    with open(filename, 'a', newline='') as file:
        csvwriter = csv.DictWriter(file, results.keys())
        csvwriter.writerow(results)


def import_csv(filename: str) -> dict:
    """Imports test results from a given csv file, and returns a dictionary of lists,
    where each list is a list of test results."""
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
    """Simulates sending data, returns a dictionary of the results."""
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
    return data_results
