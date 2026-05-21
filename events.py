import player
import adventurers

class Event:
    def __init__(self, name, description, options_func):
        self.name = name
        self.description = description
        self.options = options_func

    def get_options(self, player):
        pass
    
    def resolve(self, choice, player):
        pass

def door_options(self, player):
    opts = {
        "1": "Knock on the door.",
        "2": "Walk away."
    }
    if player.adventurer == "Scoundrel":
        opts["3"] = "Pick the lock."
    elif player.adventurer == "Sorceress":
        opts["3"] = "Freeze the lock with an ice spell."
    else: ## Is a barbarian
        opts["3"] = "Smash your way through the door."

LockedDoor = Event(
    "locked door",
    "You come across a rusted metallic door.  It's sealed shut, with a large gothic lock in the middle of it.",
    door_options
)

Cyclops = Event(
    "cyclops",
    "As you enter the sandy cave, you spot a large one eyed figure staring at you from within. He calls out: 'Who goes there!'"
)

ShadyTavern = Event(
    "shady tavern",
    "You enter the tavern and feel as if all eyes turned to you upon entering."
)
