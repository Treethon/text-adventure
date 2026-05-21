class Adventurer:
    def __init__(self, name, abilities):
        self.name = name
        self.abilities = abilities

Barbarian = Adventurer(
    "Bob the Barbarian",
    ["intimidate", "fight", "athletics", "drink", "smash"]
)

Sorceress = Adventurer(
    "Selena the Sorceress",
    ["fireball", "frostbolt", "charm", "intuition", "teleport"]
)


Scoundrel = Adventurer(
    "Sal the Scoundrel",
    ["stealth", "lockpick", "swindle", "cheapshot", "gamble"]
)
