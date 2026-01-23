import veff

class HeroStats:
    def __init__(self, health=1, endurance=1, strength=1, intelligence=1,
                 agility=1, luck=1, charisma=1):
        self.health = health
        self.endurance = endurance
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.luck = luck
        self.charisma = charisma


class Hero:
    def __init__(self, name: str, gender: str, hero_class: str, race: str):
        self.name = name
        self.gender = gender
        self.hero_class = hero_class
        self.race = race
        self.point_pool = 10
        self.stats = HeroStats()

        self.recalc_derived_stats()


    def recalc_derived_stats(self):
        self.max_hp = 5 + self.stats.health
        self.hp = min(getattr(self, "hp", self.max_hp), self.max_hp)
        self.attack = 1 + self.stats.strength
        self.defense = self.stats.endurance


    def display_stats(self):
        veff.draw_banner()
        print(f"\n{veff.Y}--- {self.name.upper()} STATS ---{veff.W}")
        veff.draw_line()
        for stat, value in vars(self.stats).items():
            label = stat.capitalize().ljust(20, ".")
            print(f"{veff.C}{label}{veff.W} {veff.G}{value}{veff.W}")
        veff.draw_line()
        print(f"Point Pool: {veff.Y}{self.point_pool}{veff.W}")


    def apply_stats(self, stat_name, amount):
        if hasattr(self.stats, stat_name) and self.point_pool >= amount:
            current_val = getattr(self.stats, stat_name)
            setattr(self.stats, stat_name, current_val + amount)
            self.point_pool -= amount
            self.recalc_derived_stats()
            print(f"{veff.G}>> Successfully added {amount} to {stat_name}!{veff.W}")
        else:
            print(f"{veff.R}!! Stat '{stat_name}' not found or insufficient points.{veff.W}")


    def display_profile(self):
        veff.draw_banner()
        print(f"{veff.Y}FINAL CHARACTER PROFILE{veff.W}".center(52))
        print(f"{veff.Y}{'═' * 30}{veff.W}".center(52))
        print(f"NAME: {veff.C}{self.name}{veff.W}".center(50))
        print(f"CLASS: {veff.C}{self.race} {self.hero_class}{veff.W}".center(50))
        print(f"GENDER: {veff.C}{self.gender}{veff.W}".center(50))
        veff.draw_line()


    def take_damage(self, raw_damage: int):
        damage = max(0, raw_damage - self.defense)
        self.hp = max(0, self.hp - damage)
        veff.type_write(f"{self.name} took {damage} damage!")
        if not self.is_alive():
            veff.type_write(f"{self.name} died")
        else:
            veff.type_write(f"{self.name} has {self.hp}/{self.max_hp} HP left")

    def is_alive(self) -> bool:
        return self.hp > 0


class Enemy:
    def __init__(self, name, basic_stats):
        self.name = name
        self.max_hp = basic_stats["hp"]
        self.hp = basic_stats["hp"]
        self.attack = basic_stats["attack"]
        self.defense = basic_stats["defense"]
        self.exp = basic_stats["exp"]

    def take_damage(self, raw_damage: int):
        damage = max(0, raw_damage - self.defense)
        self.hp = max(0, self.hp - damage)
        veff.type_write(f"{self.name} took {damage} damage!")
        if not self.is_alive():
            veff.type_write(f"{self.name} is defeated!")
        else:
            veff.type_write(f"{self.name} has {self.hp}/{self.max_hp} HP left")

    def is_alive(self) -> bool:
        return self.hp > 0
