"""
This is version 1 of my search card function,
This will ask for a monster and look at the catalogue and then return the Monster's stats
"""

import easygui
import os


catalogue = {
    "Stoneling": [7, 1, 25, 15],
    "Vexscream": [1, 6, 21, 19],
    "Dawnmirage": [5, 15, 18, 22],
    "Blazegolem": [15, 20, 23, 6],
    "Websnake": [7, 15, 10, 5],
    "Moldvine": [21, 18, 14, 5],
    "Vortexwing": [19, 13, 19, 2],
    "Rotthing": [16, 7, 4, 12],
    "Froststep": [14, 14, 17, 4],
    "Wispghoul": [17, 19, 3, 2]
}

template = ["Strength", "Speed", "Stealth", "Cunning"]


def stats_format(dictionary, message=""):
    """
    this function receives a dictionary and a message which will be formatted into a string
    for the user to read.
    """
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def search_card(card_name):
    return stats_format(catalogue[card_name], f"These are the stats for {card_name}")


easygui.msgbox(search_card(easygui.choicebox("What want search?", choices=(catalogue.keys()))))
