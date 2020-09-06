from math import sqrt
from random import randint


class Rocket:
    def __init__(self, speed=1, altitude=0, x=0):
        self.altitude = altitude
        self.x = x

        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amount=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amount)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    @staticmethod
    def getDistance(rocket1: Rocket, rocket2: Rocket):
        return sqrt((rocket1.altitude - rocket2.altitude) ** 2 + (rocket1.x - rocket2.x) ** 2)
