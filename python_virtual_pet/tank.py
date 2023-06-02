"""
tank.py
A fish tank for the virtual pet to live in.
"""
import utilities
import uuid
import json

# TODO read to tank json file when any fish is selected, store tank data
# incorporate tank into fish activities
# add option to activities to update tank

class Tank:
    """A virtual fish tank for the fish to live in.

    Attributes:
        cleanliness: int how clean is the tank from 1-10 (1o being cleanest)
        coolness: int how fun is the tank from 1-10 (10 being coolest)
    """
    # constructor method
    def __init__(self) -> None:
        self.cleanliness = 10
        self.coolness = 1
    
    @staticmethod
    def create_tank(tank_dict: dict):
        # create tank object
        tank = Tank()
        # set all attributes
        tank.cleanliness = tank_dict.get("cleanliness")
        tank.coolness = tank_dict.get("coolness")

    def store_tank_data(self) -> None:
        """ Insert tank info into the tank.json file"""
        # get the contents of tank
        tank_text = utilities.get_file_contents("data/", "tank.json")
        tank_dictionary = json.load(tank_text)

        # create a tank dict object and append it to the tank_dictionary
        tank = {
            "cleanliness": self.cleanliness,
            "coolness": self.coolness
        }
        tank_dictionary["tank"].append(tank)

        tank_json = json.dumps(tank_dictionary)

        # Save to pets.json
        with open("data/tank.json", "w") as outfile:
            outfile.write(tank_json)