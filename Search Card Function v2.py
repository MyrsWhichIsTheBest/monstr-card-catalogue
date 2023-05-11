"""
This is version 2 of my search card function,
I have
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
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def name_stats(values):
    new_stats = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
    for stat in template:
        new_stats[stat] = values[list(new_stats.keys()).index(stat)]
    return new_stats


def search_card(card_name):
    # this simple function receives the stat with the name and a message
    return stats_format(name_stats(catalogue[card_name]), f"These are the stats for {card_name}")


easygui.msgbox(search_card(easygui.choicebox("What want search?", choices=(catalogue.keys()))))
