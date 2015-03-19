class Player:

    weapons_ranged = { 'pistol': 3, 'shotgun': 2 }

    weapons_melee = { "bat": 5, "chainsaw": 4 }

    def __init__(self):
        self.health = 30
        self.bullets = 20
        self.ranged_name = "pistol"
        self.ranged_power = 3
        self.melee_name = "bat"
        self.melee_power = 5
        self.ranged_used = True


    def set_ranged(self, weapon_name):
        if weapon_name in weapons_ranged:
            self.ranged_name = weapon_name
            self.ranged_power = weapons_ranged[weapon_name]

    def set_melee(self, weapon_name):
        if weapon_name in weapons_melee:
            self.melee_name = weapon_name
            self.melee_power = weapons_melee[weapon_name]

    def lose_health(self):
        self.health -= 1
