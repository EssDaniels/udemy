import sys

evenNumbers = [element
               for element in range (100)
               if (element % 2 == 0)
               ]

evenNumbersGenerator = (element ** 2
                        for element in range (100)
                        if (element % 2 == 0)
                        )




for item in evenNumbersGenerator:
    print (item)
evenNumbersGenerator = (element ** 2
                        for element in range (100)
                        if (element % 2 == 0)
                        )

print(sum(evenNumbersGenerator))


print(sys.getsizeof(evenNumbersGenerator))

print(evenNumbers)

print(sys.getsizeof(evenNumbers))
