from src import data

crc_code = "C"
hamming_code = "H"
repetition_code = "R"


def generate_filename(code_type, bits_amount, block_size, probability):
    return f"{code_type}_{bits_amount}_{block_size}_{probability}.csv"


def get_data_from_user() -> tuple:
    """Gets data from user, in order to either do some sending data tests,
     or analyse the results of tests with given parameters."""
    code_type = input("Enter code type (Hamming - H, CRC - C, Repeating bits - R): ")
    code_type = code_type.upper()
    if code_type == "":
        return "", 0, 0, 0
    bits_amount = int(input("Enter the number of bits generated: "))
    block_size = int(input("Enter the number of bits in a packet: "))
    probability = float(input("Enter the probability (float in range [0, 1]) of distorting a single bit: "))
    return code_type, bits_amount, block_size, probability


def export():
    """Asks the user with what parameters, and how many sending data tests with them should the simulator do.
    Then exports the results to a .csv file with."""
    while True:
        code_type, bits_amount, block_size, probability = get_data_from_user()
        if code_type == "":
            break
        filename = generate_filename(code_type, bits_amount, block_size, probability)
        attempts = int(input("How many attempts? "))
        for i in range(attempts):
            random_data = data.generate_random_data(bits_amount)
            results = data.sending_data(random_data, block_size, code_type, probability)
            data.export_csv(filename, results)


def analyse():
    """Asks the user which test results to analyse, then analyses them."""
    while True:
        code_type, bits_amount, block_size, probability = get_data_from_user()
        if code_type == "":
            break
        filename = generate_filename(code_type, bits_amount, block_size, probability)
        data.analyse_data(filename)


def menu():
    """Menu where the user can choose what to do: do some sending data tests, or analyse the results of the tests."""
    answer = True
    while answer:
        answer = input("1. Export\n2. Analyse\n0. Exit\n")
        if answer == "1":
            export()
        elif answer == "2":
            analyse()
        elif answer == "0":
            answer = None


if __name__ == "__main__":
    menu()
