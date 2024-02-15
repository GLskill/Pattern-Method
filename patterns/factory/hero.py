class Hero:
    def __init__(self, race: str, clas: str, level: int, gender: str):
        self.race = race
        self.clas = clas
        self.level = level
        self.gender = gender

    def hero_say(self):
        print(f"HI, am {self.race} and {self.clas} and I am have a {self.level} level")

    def life_position(self):
        self.hero_say()
        print(f"And you can see that I am {self.gender}")

