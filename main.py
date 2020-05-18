import data

crc_code = "C"
hamming_code = "H"
repetition_code = "R"


def get_data_from_user() -> tuple:
    code_type = input("Podaj typ kodu (Hamming - H, CRC - C, Powtorzeniowy - R): ")
    code_type = code_type.upper()
    if code_type == "":
        return "", 0, 0, 0
    bits_amount = int(input("Podaj ilość bitów do wygenerowania: "))
    block_size = int(input("Podaj ilość bitów w pakiecie: "))
    prob = float(input("Podaj prawdopodobieństwo przekłamania bitu: "))
    return code_type, bits_amount, block_size, prob


def export():
    while True:
        code_type, bits_amount, block_size, prob = get_data_from_user()
        if code_type == "":
            break
        attempts = int(input("Ile prób wykonać?: "))
        for i in range(attempts):
            listt = data.generate_random_data(bits_amount)
            data.sending_data(listt, block_size, code_type, prob)


def analyse():
    while True:
        code_type, bits_amount, block_size, prob = get_data_from_user()
        if code_type == "":
            break
        filename = f"{code_type}_{bits_amount}_{block_size}_{prob}.csv"
        data.analyse_data(filename)


def menu():
    answer = True
    while answer:
        answer = input("1. Eksport\n2. Analiza\n0. Wyjście\n")
        if answer == "1":
            export()
        elif answer == "2":
            analyse()
        elif answer == "0":
            answer = None


menu()
