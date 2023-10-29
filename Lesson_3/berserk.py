from character import Character


class Berserk(Character):
    max_health = 100
    def __init__(self, name, health=100, damage=5, defence=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = self.health

    def attack(self, target):
        additional_damage_ratio = (self.max_health - self.health) / self.max_health
        real_damage = self.damage + (self.damage * additional_damage_ratio)
        return target.take_damage(real_damage)

    '''
    health = 100
    damage = 10
    
    health: 80 / 100
    damage: 10 + 2
    
    damage = base_dmg + (max_hp - hp) / max_hp * base_dmg
    base_dmg - базовый урон
    max_hp - максимальное количество здоровья
    hp - текущее здоровье
    
    '''