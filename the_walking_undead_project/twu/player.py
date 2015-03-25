# Holds all of the information for the character of each player, i.e:
# weapons available, health, weapon used. Also handles actions like decrementing
# health and switching active weapon used.
class Player:

    # A collection of all ranged weapons potentially available to the player
    weapons_ranged = { 'pistol': 3, 'shotgun': 2 }

    # A collection of all melee weapons potentially available to the player
    weapons_melee = { "bat": 5, "chainsaw": 4 }

    # Instantiates a new player with 30 health, an old revolver with 6 bullets
    # and with a score of 0
    def __init__(self):
        self.health = 30
        self.bullets = 6
        self.ranged_name = "pistol"
        self.ranged_power = 3
        self.melee_name = "bat"
        self.melee_power = 5
        self.ranged_used = True #True=ranged weapon is used, False=melee used
        self.score = 0

    # If ranged weapon supplied is in the list of supported ones,
    # makes the player use that weapon
    def set_ranged(self, weapon_name):
        if weapon_name in weapons_ranged:
            self.ranged_name = weapon_name
            self.ranged_power = weapons_ranged[weapon_name]

    # If melee weapon supplied is in the list of supported ones,
    # makes the player use that weapon
    def set_melee(self, weapon_name):
        if weapon_name in weapons_melee:
            self.melee_name = weapon_name
            self.melee_power = weapons_melee[weapon_name]

    # Switches whether the player uses their melee or ranged weapon
    def switch_active(self):
        self.ranged_used = not self.ranged_used

    # Decrements player's health by the given amount
    # If damage is more than the players remaining health
    # a PlayerIsDead exception is raised
    def lose_health(self, damage):
        if self.health > damage:
            self.health -= damage
        else:
            raise PlayerIsDead("Game Over")
