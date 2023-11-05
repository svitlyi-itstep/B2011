from character import Character
from berserk import Berserk
import random

def fight(players, max_rounds=100):
    if len(players) < 2:
        raise ValueError('Недостаточно бойцов для начала боя!')

    print('Бойцы:')
    for player in players:
        print(player, '\n')

    rounds = 0
    while True:
        if rounds > max_rounds:
            raise RuntimeError('Слишком много раундов!')
        for player in players:
            # enemy = random.choice(list(filter(lambda item: item != player, players)))
            # players.remove(player)
            enemy = random.choice(players)
            # players.append(player)
            player_dmg = player1.attack(enemy)

            print(f'{player.name} атаковал {enemy.name} и нанёс {round(player_dmg, 1)} урона.')
            print(f'У {enemy.name} осталось {round(enemy.health, 1)} здоровья.')
            print()

        players_alive = 0
        for player in players:
            players_alive += int(player.alive())

        # players_alive = sum([player.alive() for player in players])

        if players_alive <= 1:
            break

        rounds += 1

    print('Бойцы:')
    for player in players:
        print(player, '\n')


player1 = Berserk(name='Петя', health=100,
                    damage=0, defence=0)
player2 = Character('Вася', health=999999999, damage=1)
player3 = Character('Анатолий')

try:
    fight([])
except ValueError:
    fight([player1, player2])


'''
    Поменять программу таким образом, чтобы персонажи атаковали друг друга 
    до тех пор, пока у одного из них не закончится здоровье.
'''

