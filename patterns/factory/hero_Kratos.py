from hero import Hero


class Kratos(Hero):

    def __init__(self, race: str, clas: str, level: int, gender: str = "God of War"):
        super().__init__(race, clas, level, gender)

