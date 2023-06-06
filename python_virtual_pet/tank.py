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

    def load_tank_data(self) -> None:
        tank = utilities.get_file_contents("data/", "tank.json")
        tank_dictionary = json.loads(tank)
        self.cleanliness = tank_dictionary.get("cleanliness")
        self.coolness = tank_dictionary.get("coolness")


    def store_tank_data(self) -> None:
        """ Insert tank info into the tank.json file"""
        # get the contents of tank
        tank_text = utilities.get_file_contents("data/", "tank.json")
        tank_dictionary = json.loads(tank_text)

        tank_dictionary["cleanliness"] = self.cleanliness
        tank_dictionary["coolness"] = self.coolness

        tank_json = json.dumps(tank_dictionary)

        # Save to pets.json
        with open("data/tank.json", "w") as outfile:
            outfile.write(tank_json)

if __name__ == "__main__":
    t1 = Tank()
    print(t1.cleanliness)
    print(t1.coolness)
    t1.store_tank_data()
    print(t1.cleanliness)
    print(t1.coolness)
