# funkcja generująca liczby które są mnożone przez siebie

def generate_number_mux_itself(numberStart=1):
    while True:
        element = numberStart * numberStart
        yield element
        numberStart += 1


generateNumbers = []
number_generate = generate_number_mux_itself(30)

for _ in range(20):  # underscore _ informuje o zmiennej która nie bedzie dalej uzywana

    generateNumbers.append(next(number_generate))

print(generateNumbers)

for _ in range(30):  # underscore _ informuje o zmiennej ktora nie bedzie dalej uzywana

    generateNumbers.append(next(number_generate))

print(generateNumbers)

