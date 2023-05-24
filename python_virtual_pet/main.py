""" The Virtual Pet Program """

import utilities
import json
import pet
from pet import Pet

def main():
    active_pets = []
    # Create a menu for pet playgroud
    new_menu = """
    Here is your list of options:
        1 - Option 1: Create a new pet
        2 - Option 2: Select your pet to interact with
        3 - Option 3: Save pet data
        4 - Option 4: Quit
    """

    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        if choice == "1":
            pet = create_new_pet()
            active_pets.append(pet)
        elif choice == "2":
            pets = utilities.get_file_contents("data/", "pets.json")
            pets = json.loads(pets)
            pets =  pets.get("pets")
            
            # Loop though all pets asking if the user wants to play with one
            # of the pets.
            #IF yes, append that pet to active_pets and break
            for pet in pets:
                name = pet.get("name")
                play_with = input(f"Would you like to play with {name}? (y/n) ")
                if play_with == "y":
                    # create a pet object with the data
                    new_pet = Pet.create_pet(pet)

                    # append pet to active_pets
                    active_pets.append(new_pet)

                    # play with the chosen pet
                    
            if not active_pets:
                print("\nYou have no pets to play with.")
                print("Try creating a new pet!")
        elif choice == "3":
            if active_pets:
                for pet in active_pets:
                    pet.store_pet_data()
    print("\nThanks for playing!")

def create_new_pet():
    """ create a and returns a new pet object"""
    name = input("Select aname for your pet: ")
    pet = Pet(name)
    return pet

if __name__== "__main__":
    main()