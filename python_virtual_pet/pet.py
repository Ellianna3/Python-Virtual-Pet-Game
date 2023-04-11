"""
pet.py
by Ellianna Bauer
A virtual pet complete with pet emotions and behavior.
"""
import utilities
import random

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
        tiredness: int how tired is the pet 0-10 (10 being most tired)
    """
    # constructor method
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed
        self.nicknames = []
        self.happiness = 5
        self.hunger = 4
        self.health = 5
        self.boredom = 5
        self.tiredness = 0

    def play(self):
        """let the user choose how to play with the pet"""
        menu = f"\nChoose an option for playing with {self.name}:\n"
        menu += "\n\t1 - play fetch\n\t2 - chase the laser pointer"
        menu += "\n\t3 - tug of war\n\t4 - quit"

        choice = ""
        description = ""
        while choice != "4":
            choice = utilities.get_menu_choice(menu, ("1", "2", "3", "4"))
            if choice == "1":
                description = f"{self.name} runs after the toy you toss."
                if random.choice("01") == "1":
                    description += f"Once {self.name} grabs the toy,"
                    description += f"{self.name} runs away with it."
                    self.happiness += 1
                    # quit since the pet ran off with the toy
                    choice = "4"
                else:
                    description += f"{self.name} runs after the toy and picks"
                    description += "it up and brings it back to you."
                    description += f"{self.name} really likes this game."
                    self.happiness += 2
            elif choice == "4":
                description += f"{self.name} goes back to their favorite spot."
                description += "You are done playing."
            else:
                description = f"{self.name} says weeee!!!"
                self.happiness += 1
            
            # play affects other attributes
            self.hunger += 1
            self.tired += 1

            # keep happiness capped at 10
            if self.happiness > 10:
                self.happiness = 10
            print(description)

            # we're done playing - provide update
            description += f"{self.name}'s happiness is at {self.happiness}"
            print(description)

# global scope
if __name__ == "__main__":
    # Construct 2 pet instances
    fluffy = Pet("Fluffy", "rock")