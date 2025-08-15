from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points, damage_points):
        super().__init__(type_of_enemy = 'Zombie', health_points = health_points, damage_points = damage_points)


    def talk(self):
        print("*Grumbling...*")

    def spread_poison(self):
        print("The Zombie is spreading poison!!!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print("The Zombie regenerated 2 health points.")