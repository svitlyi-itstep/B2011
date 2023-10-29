class Character:
    name = ''
    health = 100
    damage = 5
    defence = 0

    def __init__(self, name, health=100, damage=5, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return f' - {self.name} -\n' \
               f' Здоровье: {self.health}\n' \
               f' Урон: {self.damage}\n' \
               f' Защита: {self.defence}'

    def take_damage(self, damage):
        damage = max(damage, 0)
        self.health -= damage
        return damage

    def attack(self, target):
        return target.take_damage(self.damage)