import time

a = int(input("Podaj liczbe do której mają być sumowane "))



def sumuj_do(number):

    suma = 0

    for number in range(number+1):
            suma = suma + number

    return suma

def sumuj_do2(number):

    return sum([number for number in range(number+1)])
def sumuj_do3(number):

    return sum({number for number in range(number+1)})
def sumuj_do4(number):

    return sum((number for number in range(number+1)))

def sumuj_do5(number):
    return (1+number) / 2 * number
def finish_timer(start):
    stop = time.perf_counter()
    return stop-start

def function_performence(func, arg, how_many_time = 1):
    start = time.perf_counter()
    func(arg)
    stop = time.perf_counter()
    return stop - start

# Przekazywanie funkcji do funkcji

print(function_performence(sumuj_do, a))
print(function_performence(sumuj_do2, a))
print(function_performence(sumuj_do3, a))
print(function_performence(sumuj_do4, a))
print(function_performence(sumuj_do5, a))

def suma(*arg):
    return sum(*arg)

print(suma(count(2,4,2,4,5,10)))