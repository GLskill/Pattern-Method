from hero import Hero
from hero_Kratos import Kratos
from hero_Tanos import Tanos
from hero_Wooki import Wooki
from hero_Yoda import Yoda


class HeroFactory:

    def hero_by_type(self, hero_type: str):
        if hero_type == "Kratos":
            return Kratos(race="human", clas="warior", level=65)
        if hero_type == "Tanos":
            return Tanos(race="titan", clas="manipulator", level=99)
        if hero_type == "Wooki":
            return Wooki(race="beast", clas="archer", level=38)
        if hero_type == "Yoda":
            return Yoda(race="humanoid", clas="jedi master", level=105)
        else:
            print("There is no such hero in this universe")
            print("-----Choose another hero or another universe-----")
            return Hero(gender="null", race="null", clas="null", level=0)


if __name__ == "__main__":

    hero_factory = HeroFactory()

    null_hero = hero_factory.hero_by_type("null")
    kratos_hero = hero_factory.hero_by_type("Kratos")
    tanos_hero = hero_factory.hero_by_type("Tanos")
    wooki_hero = hero_factory.hero_by_type("Wooki")
    yoda_hero = hero_factory.hero_by_type("Yoda")

    print("________________________________________________________")
    kratos_hero.life_position()
    print("________________________________________________________")
    tanos_hero.life_position()
    print("________________________________________________________")
    wooki_hero.life_position()
    print("________________________________________________________")
    yoda_hero.life_position()
    print("________________________________________________________")
    null_hero.life_position()
    print("________________________________________________________")

