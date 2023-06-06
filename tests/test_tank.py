from python_virtual_pet import tank
# from python_virtual_pet import utilities
from pathlib import Path
import json
import pytest

t1 = tank.Tank()

def setup():
    test_file = '{"tanks":{"cleanliness": 10, "coolness": 10}}'

    #create a new json file
    # Save to pets.json
    with open("data/test_tank.json", "w") as outfile:
        outfile.write(test_file)

