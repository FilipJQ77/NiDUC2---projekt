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
    code_type = True
    while code_type:
        code_type, bits_amount, block_size, prob = get_data_from_user()
        attempts = int(input("Ile prób wykonać?: "))
        for i in range(attempts):
            listt = data.generate_random_data(bits_amount)
            data.sending_data(listt, block_size, code_type, prob)


def analyse():
    code_type = True
    while code_type:
        code_type, bits_amount, block_size, prob = get_data_from_user()
        filename = f"{code_type}_{bits_amount}_{block_size}_{prob}.csv"
        data.analyse_data(filename)


def menu():
    answer = True
    while answer:
        print("1. Eksport\n2. Analiza\n0. Wyjście")
        answer = input()
        if answer == "1":
            export()
        elif answer == "2":
            analyse()
        elif answer == "0":
            answer = None
        else:
            print("Niepoprawna opcja")


menu()

correct = "Correct"
fixed = "Fixed"
repeat = "Repeat"
wrong = "Wrong"

dicto = {correct: [9, 8, 7, 6, 0, 9, 9, 8],
         fixed: [0, 1, 3, 3, 7, 0, 1, 1],
         repeat: [0, 1, 3, 2, 2, 2, 4, 5],
         wrong: [1, 1, 0, 1, 3, 1, 0, 1]}
data.analyse(dicto)

# data.analyse_data("H_400_4_0.01.csv")
