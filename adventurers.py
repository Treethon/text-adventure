class Adventurer:
    def __init__(self, name, abilities):
        self.name = name
        self.abilities = abilities

Barbarian = Adventurer(
    "Barbarian",
    ["intimidate", "fight", "athletics", "drink", "smash"]
)

Sorceress = Adventurer(
    "Sorceress",
    ["fireball", "frostbolt", "charm", "intuition", "teleport"]
)


Scoundrel = Adventurer(
    "Scoundrel",
    ["stealth", "lockpick", "swindle", "cheapshot", "gamble"]
)
