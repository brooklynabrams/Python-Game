from Enemy import *
import random

class Vampire(Enemy):
    def __init__(self, health_points, damage_points):
        super().__init__(type_of_enemy = 'Vampire', health_points = health_points, damage_points = damage_points)

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.health_points += 9
            print("The Vampire regenerated 9 health points.")