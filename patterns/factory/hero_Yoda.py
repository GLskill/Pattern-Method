from hero import Hero


class Yoda(Hero):

    def __init__(self, race: str, clas: str, level: int, gender: str = "The Jedi Master"):
        super().__init__(race, clas, level, gender)

