"""
This is version 8 of my Add Card Function in python
This function asks the user for the name of the new card and asks for the stats of that card too.
This is my trialling for add card function, for the function I ultimately went with, go to v7
"""
import easygui


def stats_format(dictionary, message=""):
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def add_card(name, new_stats):
    for stat_name in list(new_stats.keys()):
        while True:
            value = easygui.integerbox(f"Enter the {stat_name} stat (1-25): ")
            if 1 <= value <= 25:
                new_stats[stat_name] = value
                break
            else:
                easygui.msgbox("Please only input whole numbers", ok_button="Ugh Fine...")
                # error message
    return [name, new_stats]


template = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
output = add_card(easygui.enterbox("What is the name of the new card?"), template)
# format dictionary to print out
# catalogue.update({output[0]: list(output[1].values())})
# this code above adds the output to the catalogue (aka monster_card_dictionary v1)
easygui.msgbox(stats_format(output[1], f"You successfully created a New Monster Card: {output[0]}"))
# output is the return of the add_card() function which returns the stats and the name

