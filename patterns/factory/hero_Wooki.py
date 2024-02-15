from hero import Hero


class Wooki(Hero):

    def __init__(self, race: str, clas: str, level: int, gender: str = "Do not jump to conclusions"):
        super().__init__(race, clas, level, gender)

