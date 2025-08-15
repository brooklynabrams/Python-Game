from Enemy import *
from Mutant import Mutant
from Ogre import Vampire
from Zombie import Zombie
from Hero import *
from Weapon import *

print(
    "Choose which two to battle:\n"
    "1. Mutant (50 HP, 5 Damage)\n"
    "2. Zombie (30 HP, 3 Damage)\n"
    "3. Vampire (100 HP, 1 Damage)\n"
    "4. Hero (100 HP, 8 Damage)\n"
)

choice1 = input("Enter the first character (all lowercase): ")
choice2 = input("Enter the second character (all lowercase): ")


def battle(e1: Enemy, e2: Enemy):

    while e1.health_points > 0 and e2.health_points > 0:
        print('-------------')
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type()}: {e1.health_points} HP left")
        print(f"{e2.get_type()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points -= e2.damage_points
        e1.attack()
        e2.health_points -= e1.damage_points
    print('-------------')

    if e1.health_points > 0:
        print(f"{e1.get_type()} wins!")
    else:
        print(f"{e2.get_type()} wins!")


def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('-------------')
        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type()}: {enemy.health_points} HP left")
        enemy.attack()
        hero.health_points -= enemy.damage_points
        hero.attack()
        enemy.health_points -= hero.damage_points
    print('-------------')

    if hero.health_points > 0:
        print(f"Hero wins!")
    else:
        print(f"{enemy.get_type()} wins!")


if choice1== "hero":
    choice1 = Hero(100, 8)

if choice2== "hero":
    choice2 = Hero(100, 8)

if choice1== "mutant":
    choice1 = Mutant(50, 5)

if choice2== "mutant":
    choice2 = Mutant(50, 5)

if choice1== "zombie":
    choice1 = Zombie(30, 3)

if choice2== "zombie":
    choice2 = Zombie(30, 3)

if choice1 == "vampire":
        choice1 = Vampire( 100, 1)

if choice2 == "vampire":
        choice2 = Vampire( 100, 1)


if isinstance(choice1, Hero) or isinstance(choice2, Hero):
    hero_battle(choice1, choice2)
else :
    battle(choice1, choice2)
