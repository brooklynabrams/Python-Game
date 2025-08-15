from Enemy import *
import random
class Mutant(Enemy):
    def __init__(self, health_points, damage_points):
        super().__init__(type_of_enemy ='Mutant', health_points = health_points, damage_points = damage_points)

    def talk(self):
        print("I'm a mutant of all enemies. Be prepared to DIE.")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.30
        if did_special_attack_work:
            self.damage_points += 2
            print("The Mutant is angry. Damage points increased by 2.")