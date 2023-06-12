"""
pet.py
by Ellianna Bauer
A virtual pet complete with pet emotions and behavior.
"""
import utilities
import random
import uuid
import json

class Pet: 
    """A virtual fish (can be used as a base class for other pet types).

    Attributes:
        name: str
        nicknames: list (a list strings of given nicknames for your fish)
        happiness: int how happy is the pet from 0-10 (10 being happiest)
        hunger: int how hungry is the pet from 0-10 (10 being hungriest)
        health: int how healthy is the pet 0-10 (10 being healthiest)
        boredom: int how bored is the pet 0-10 (10 being most bored)
        tiredness: int how tired is the pet 0-10 (10 being most tired)
    """
    # constructor method
    def __init__(self, name: str) -> None:
        self.name = name
        self.ID = uuid.uuid1().hex
        self.nicknames = []
        self.happiness = 5
        self.hunger = 4
        self.health = 5
        self.boredom = 5
        self.tiredness = 0

    def store_pet_data(self) -> None:
        """ Insert pet information into the pets.json file"""
        # get the contents of the pets
        pets_text = utilities.get_file_contents("data/", "pets.json")
        pets_dictionary = json.loads(pets_text)

        # create a pet dictionary object and append it to the pet_dictionary
        this_pet = {
            "name": self.name,
            "ID": self.ID,
            "nicknames": self.nicknames,
            "happiness": self.happiness,
            "hunger": self.hunger,
            "health": self.health,
            "boredom": self.boredom,
            "tiredness": self.tiredness
        }
        pets_dictionary["pets"].append(this_pet)

        pets_json = json.dumps(pets_dictionary)

        # Save to pets.json
        with open("data/pets.json", "w") as outfile:
            outfile.write(pets_json)

    @staticmethod
    def load_pet() -> None:
        """Grab pet data from the pets.json file and get the attributes."""

        # Get all the pets from pets.json
        pets = utilities.get_file_contents("data/", "pets.json")
        pets_dictionary = json.loads(pets)
        all_pets = pets_dictionary.get("pets")

    @staticmethod
    def get_pet():
        """Show user list of pets and allow them to select a pet to play with."""
        # Get all the pets from pets.json
        pets = utilities.get_file_contents("data/", "pets.json")
        pets_dictionary = json.loads(pets)
        all_pets = pets_dictionary.get("pets")

        # show list of pets and let the user select a pet
        for pet in all_pets:
            print(pet.get["name"])

        # create and return a pet
    
    @staticmethod
    def create_pet(pet_dict: dict):
        # get pet name
        name = pet_dict.get("name")

        # create pet object
        pet = Pet(name)

        # set all pet attributes
        pet.ID = pet_dict.get("ID")
        pet.nicknames = pet_dict.get("nicknames")
        pet.happiness = pet_dict.get("happiness")
        pet.hunger = pet_dict.get("hunger")
        pet.health = pet_dict.get("health")
        pet.boredom = pet_dict.get("boredom")
        pet.tiredness = pet_dict.get("tiredness")

        return pet

    # main menu
    def choose_action(self):
        """The user can choose to do five things with their fish.
        They can play with the fish, clean the fish's tank, feed the fish,
        or sell the fish, aka quit. This function is just the gateway to 
        all of the options, and tells the user which function they have selected.
        """
        menu = f"\nChoose what to do next with {self.name}:\n"
        menu += f"\n\t1 - Play with {self.name}\n\t2 - Photograph {self.name}"
        menu += f"\n\t3 - Feed {self.name}\n\t4 - Display {self.name}'s stats"
        menu += f"\n\t5 - Stop interacting with {self.name} (Quit)\n"
        
        choice = ""
        while choice != "5":
            choice = utilities.get_menu_choice(menu, ("1", "2", "3", "4", "5"))
            if choice == "1":
                print(f"\n{self.name} is excited to play!")
                self.play()
            elif choice == "2":
                print(f"\nYou have decided to take a picture of {self.name}.")
                self.picture()
            elif choice == "3":
                print(f"\nYou have decided to feed {self.name}.")
                self.feed()
            elif choice == "4":
                print(f"\nYou have decided to check up on {self.name}.")
                self.check_stats()
            elif choice == "5":
                print(f"\nHeading back to main menu, don't forget ")
                print(f"to save {self.name}'s data.")

    # clean the fish's tank, improve health and happiness
    def picture(self):
        desc = f"\nYou grab your phone and pull up the camera app. {self.name} "
        desc += f"seems to know what you are doing and poses. It turns out great!"
        print(desc)
        self.health += 1
        if self.health > 10:
            self.health = 10

    # feed the fish, improve hunger and tiredness
    def feed(self):
        desc = "\nYou drop a bit of fish food into the tank. "
        desc += f"{self.name} swims to the top of the tank and eats it!"
        print(desc)
        self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0

    # check all of the attributes of the fish
    def check_stats(self):
        description = f"\nHere are {self.name}'s stats:"
        description += f"\n\tHappiness: {self.happiness}/10"
        description += f"\n\tHunger: {self.hunger}/10"
        description += f"\n\tHealth: {self.health}/10"
        description += f"\n\tBoredom: {self.boredom}/10"
        description += f"\n\tTiredness: {self.tiredness}/10"
        print(description)
        
    # play with the fish
    def play(self):
        """let the user choose how to play with their fish"""
        menu = f"\nChoose an option for playing with {self.name}:\n"
        menu += "\n\t1 - play fetch\n\t2 - follow your finger"
        menu += "\n\t3 - swim through the hoop\n\t4 - quit"

        choice = ""
        description = ""
        while choice != "4":
            choice = utilities.get_menu_choice(menu, ("1", "2", "3", "4"))
            if choice == "1":
                description += "\nYou toss a very small stick into the far "
                description += "corner of the tank. "
                if random.choice("01") == "1":
                    description += f"{self.name} runs after the stick you toss. "
                    description += f"Once {self.name} grabs the stick, "
                    description += f"{self.name} swims away and hides it in "
                    description += f"{self.name}'s favorite tank plant. "
                    self.happiness += 1
                    self.hunger += 1
                    self.tiredness += 1
                    self.boredom -= 1
                    # quit since the pet ran off with the toy
                    choice = "4"
                else:
                    description += f"{self.name} runs after the stick, picks "
                    description += "it up, and brings it back to you. "
                    description += f"{self.name} swims in a little circle "
                    description += "and makes a few small bubbles. "
                    description += f"{self.name} really likes this game! "
                    self.happiness += 2
                    self.hunger += 1
                    self.tiredness += 1
                    self.boredom -= 1
            elif choice == "2":
                description += "\nYou hold your finger up to the glass of "
                description += f"{self.name}'s tank and draw a path. "
                description += f"{self.name} follows your finger. "
                description += f"{self.name} finds this intellectually stimulating. "
                self.happiness += 1
                self.hunger += 1
                self.tiredness += 1
                self.boredom -= 2
            elif choice == "3":
                description += "\nYou take a small plastic (but fish safe) ring and "
                description += "hold it just above the surface of the water. "
                description += f"{self.name} gets a 'running' start and jumps "
                description += "out of the water through the hoop! "
                self.happiness += 1
                self.hunger += 1
                self.tiredness += 2
                self.boredom -= 1
            elif choice == "4":
                description += f"{self.name} goes back to their favorite spot. "
                description += "You are done playing. "

            # keep attributes capped
            if self.happiness > 10:
                self.happiness = 10
            if self.boredom < 0:
                self.boredom = 0
            if self.hunger > 10:
                self.hunger = 10

            # we're done playing - provide update
            description += f"\n\n{self.name}'s happiness is at {self.happiness}, "
            description += f"hunger is at {self.hunger}, "
            description += f"tiredness is at {self.tiredness}, and "
            description += f"boredom is at {self.boredom}. "
            print(description)
            description = ""

# global scope
if __name__ == "__main__":
    # Construct pet instances
    fish_name = input("\nWhat would you like your fish to be named?: ")
    fish_name = fish_name.capitalize()
    user_pet = Pet(fish_name)

    user_pet.choose_action()