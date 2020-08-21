from math import pi

def pole_prostokata(bok_a, bok_b):
    return bok_b*bok_a


def pole_kwadratu(bok_a):
    return bok_a*bok_a

def pole_trojkata(podstawa, wysokosc):
    return podstawa*wysokosc/2

def pole_trapezu(bok_a, bok_b,h):
    return (bok_a+bok_b)*h/2

def pole_kola(r):
    return pi*r**2