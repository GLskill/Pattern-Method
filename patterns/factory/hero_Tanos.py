from hero import Hero


class Tanos(Hero):

    def __init__(self, race: str, clas: str, level: int, gender: str = "A supervillain"):
        super().__init__(race, clas, level, gender)

