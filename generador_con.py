import random


def generate_password():
    capital_letters = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'V', 'X', 'Y', 'Z']
    lowercase_letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars = ['!', '"', '£', '$', '%', '&', '/', '(', ')', '=', '?', '^', 'é', '*', 'ç', '§', '.', ',', ':', '-', '_', '|', '#', '@', '+']

    caracteres = capital_letters + lowercase_letters + numbers + chars

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password


def run():
    password = generate_password()
    print('Tu nueva password es: ' + password)


if __name__ == '__main__':
    run()


