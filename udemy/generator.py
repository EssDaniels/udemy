import sys



evenNumbersGenerator = (element
                        for element in range(471)
                        if (element % 7 == 0 and not element % 5 == 0)
                            if(element > 99 and element < 471)

                        )

for item in evenNumbersGenerator:
    print(item)



