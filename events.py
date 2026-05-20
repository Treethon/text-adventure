import player

class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_options(self, player):
        pass
    
    def resolve(self, choice, player):
        pass

LockedDoor = Event(
    "locked door",
    "You come across a rusted metallic door.  It's sealed shut, with a large lock in the middle of it."
)

Cyclops = Event(
    "cyclops",
    "As you enter the sandy cave, you spot a large one eyed figure staring at you from within. He calls out: 'Who goes there!'"
)

ShadyTavern = Event(
    "shady tavern",
    "You enter the tavern and feel as if all eyes turned to you upon entering."
)
