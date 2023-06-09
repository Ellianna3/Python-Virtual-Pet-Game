""" The Virtual Pet Program """

import utilities
import json
import pet
from pet import Pet
from tank import Tank

new_menu = """
    Here is your list of options:
        1 - Option 1: Buy a new fish
        2 - Option 2: Select your fish to interact with
        3 - Option 3: Save fish and tank data
        4 - Option 4: Clean your fish tank
        5 - Option 5: Quit
    """

def main():
    pet = None
    tank = get_tank()

    # Create a menu for pet playgroud
    options = ("1", "2", "3", "4", "5")
    choice = ""
    while choice != "5":
        choice = utilities.get_menu_choice(new_menu, options)
        
        if choice == "1":
            pet = create_new_pet()
            pet = interact_with_pet(pet)

        elif choice == "2":
            pets = get_pets()
            # retrieve a pet to play with
            pet = get_pet(pets)
            # redundancy
            if not pet:
                print("\nYou have no fish to play with.")
                print("Try buying a new fish!")
                continue
            # use choose_action from pet.py
            pet = interact_with_pet(pet)

        elif choice == "3":
            if pet:
                pet.store_pet_data()
                tank.store_tank_data()
                print("The fish's data has been saved.")

        elif choice == "4":
            tank.cleanliness += 2
            if tank.cleanliness > 10:
                tank.cleanliness = 10
            print("\nYour fish will appreciate a clean tank!")

    print("\nThanks for playing!")

def get_tank():
    tank = Tank()
    tank.load_tank_data()
    return tank

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
    name = input("Select a name for your fish: ")
    pet = Pet(name)
    return pet

if __name__== "__main__":
    main()