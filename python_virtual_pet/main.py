""" The Virtual Pet Program """

import utilities
import json
import pet
from pet import Pet
from tank import Tank

new_menu = """
    Here is your list of options:
        1 - Option 1: Create a new pet
        2 - Option 2: Select your pet to interact with
        3 - Option 3: Save pet data
        4 - Option 4: Quit
    """

def main():
    pet = None
    tank = None

    # Create a menu for pet playgroud
    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        
        if choice == "1":
            pet = create_new_pet()
            # if there is a tank, use it, if not, make a new one
            if tank == None:
                tank = create_new_tank()
            else:
                tank = get_tank()
            pet = interact_with_pet(pet)

        elif choice == "2":
            pets = get_pets()
            # retrieve a pet to play with
            pet = get_pet(pets)
            # redundancy
            if not pet:
                print("\nYou have no pets to play with.")
                print("Try creating a new pet!")
                continue
            # retrieve tank
            tank = get_tank()
            # use choose_action from pet.py
            pet = interact_with_pet(pet)

        elif choice == "3":
            if pet:
                pet.store_pet_data()
                tank.store_tank_data()
                print("The fish's data has been saved.")

    print("\nThanks for playing!")

def interact_with_pet(pet):
    """interact with the pet"""
    pet.choose_action()
    return pet

def get_pet(pets):
    for pet in pets:
        name = pet.get("name")
        prompt = (f"Would you like to play with {name}? (y/n)")
        play_with = utilities.get_menu_choice(prompt, ("y", "n"))
        if play_with == "y":
            # create a pet object with the data
            new_pet = Pet.create_pet(pet)
            return new_pet
    return None

def get_pets() -> list:
    """load the pets from the pets.json file
    Returns:
        pets: a list of pet objects
    """
    pets = utilities.get_file_contents("data/", "pets.json")
    pets = json.loads(pets)
    pets =  pets.get("pets")
    return pets

def create_new_pet():
    """ create a and returns a new pet object"""
    name = input("Select a name for your pet: ")
    pet = Pet(name)
    return pet

def create_new_tank():
    tank = Tank()
    return tank

def get_tank():
    tank = utilities.get_file_contents("data/", "tank.json")
    tank = json.load(tank)
    new_tank = Tank.create_tank(tank)
    return new_tank

if __name__== "__main__":
    main()