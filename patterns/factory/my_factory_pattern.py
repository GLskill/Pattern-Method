from enum import Enum
from math import *


class Coordinate(Enum):
    CARTES = 5
    POLAR = 9
    BRAVO = 21


class Proger:
    def __init__(self, june, middle, senior):
        self.june = june
        self.middle = middle
        self.senior = senior

    def str(self):
        return f'june: {self.june}, middle:{self.middle}, senior:{self.senior}'

    @staticmethod
    def new_cartes_status(june, middle, senior):
        return Proger(june, middle, senior)

    @staticmethod
    def new_polar_status(rho, theta, beta):
        return Proger(rho * cos(theta), rho * sin(theta), rho * tan(beta))


if __name__ == '__main__':
    p = Proger(5, 8, 13)
    p2 = Proger.new_polar_status(3, 13, 16)

    print(p, p2)
