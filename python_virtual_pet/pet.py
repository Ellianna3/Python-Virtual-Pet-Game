"""
pet.py
by Ellianna Bauer
A virtual pet complete with pet emotions and behavior.
"""

class Pet: 
    """A virtual pet (can be used as a base class for other pet types).

    Attributes:
        name: str
        breed: str
        nicknames: list (a list strings of given nicknames for your pet)
        happiness: int how happy is the pet from 0-10 (10 being happiest)
        hunger: int how hungry is the pet from 0-10 (10 being hungriest)
        health: int how healthy is the pet 0-10 (10 being healthiest)
        boredom: int how bored is the pet 0-10 (10 being most bored)
    """

    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed
        self.nicknames = []
        self.happiness = 5
        self.hunger = 4
        self.health = 5
        self.boredom = 5

# global scope
if __name__ == "__main__":
    # Construct 2 pet instances
    fluffy = Pet("Fluffy", "rock")
    lesser_fluffy = Pet("Lesser Fluffy", "mold")
    
# Show some pet stats
    print(f"Our first pet is {fluffy.name}")
    print(f"{fluffy.name} is a {fluffy.breed}.")
    print(f"Our other pet is {lesser_fluffy.name}")
    print(f"{lesser_fluffy.name} is a {lesser_fluffy.breed}.")