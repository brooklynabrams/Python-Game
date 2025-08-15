class Enemy:

    type_of_enemy: str
    health_points: int
    damage_points: int

    def __init__(self, type_of_enemy, health_points, damage_points):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.damage_points = damage_points

    def get_type(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight.")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.damage_points} damage.")