"""
This is version 8 of my Add Card Function in python
This function asks the user for the name of the new card and asks for the stats of that card too.
This is my trialling for add card function
"""
import easygui


def add_card(name):
    stats = {}
    for stat_name in ["Strength", "Speed", "Stealth", "Cunning"]:
        while True:
            value = input(f"Enter the {stat_name} stat (1-25): ")
            if value.isdigit() and 1 <= int(value) <= 25:
                stats[stat_name] = int(value)
                break
            else:
                print("Please enter a valid integer between 1 and 25.")

    return {name: list(stats.values())}


print(add_card(easygui.enterbox("What name?")))
