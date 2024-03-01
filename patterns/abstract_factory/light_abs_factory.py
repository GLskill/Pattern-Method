from abc import ABC


class HomePets(ABC):
    def consume(self):
        pass


class Cats(HomePets):
    def consume(self):
        print("63% of people keep cats at home")


class Dogs(HomePets):
    def consume(self):
        print("47% of people keep dogs at home")


class HomePetsFactory(ABC):
    def prepare(self, amount):
        print()