"""
This is version 4 of my search card function,
I have added name stats function v3
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

template = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}


def stats_format(dictionary, message=""):
    """
    this function receives a dictionary and a message which will be formatted into a string
    for the user to read.
    """
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def name_stats(values):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(template.keys())
    new_stats = dict(zip(stat_names, values))
    return new_stats


def search_card(card_name):
    """
    This simple function receives the stat with the name and a message
    """
    return stats_format(name_stats(catalogue[card_name]), f"These are the stats for {card_name}")


easygui.msgbox(search_card(easygui.choicebox("What want search?", choices=(catalogue.keys()))))
