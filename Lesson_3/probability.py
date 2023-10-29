import random

def roll_chance(probability):
    return random.randint(1, 100) < probability

for _ in range(10):
    print(roll_chance(90))