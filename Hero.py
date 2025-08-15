from Weapon import *

class Hero:
    def __init__(self, health_points, damage_points):
        self.health_points = health_points
        self.damage_points = damage_points
        self.is_weapon_equipped = False
        self.weapon: Weapon = None


    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.damage_points += self.weapon.attack_increase
            self.is_weapon_equippedn = True

    def attack(self):
        print(f"Hero attacks for {self.damage_points}.")