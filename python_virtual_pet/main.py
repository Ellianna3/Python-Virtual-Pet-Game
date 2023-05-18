""" The Virtual Pet Program """

import utilities
import pet

def main():
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

    print("\nThanks for playing!")


if __name__== "__main__":
    main()