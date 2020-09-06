def generate_even_numbers():
    for element in range(400):
        if (element % 2) == 0:
            yield element  # zatrzymuje funkcje w tym miejscu i po ponowny wywołaniu startuje od tego miejsca


evenNumbersGenerate = (element
                       for element in range(400)
                       if (element % 2 == 0))

print(evenNumbersGenerate)

