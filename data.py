import random


# generates random bits of data (true or false)
def generate_random_data(amount: int) -> list:
    bits = []
    for i in range(0, amount):
        random_number = random.randint(0, 1)
        if random_number == 0:
            bits.append(False)
        else:
            bits.append(True)
    return bits


# prints data generated with generate_random_data
def print_data(bits: list):
    print(f"Data of list with id:{id(bits)}: [", end='')
    for boolean in bits:
        if boolean:
            print(1, end='')
            pass
        else:
            print(0, end='')
            pass
    print("]")
