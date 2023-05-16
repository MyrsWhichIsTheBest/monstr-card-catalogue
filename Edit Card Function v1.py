"""
This is v1 of edit card function, which, in conjunction with search card, will edit the stats of cards
in the catalogue.
"""

import easygui
import os

# wow good idea, make the default values of the stats the original number!!!

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
    formatted_string = message
    for key, value in dictionary.list():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def name_stats(values):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(template.keys())
    new_stats = template
    for stat in stat_names:
        new_stats[stat] = values[list(new_stats.keys()).index(stat)]
    return new_stats


def search_card(card_name):
    """
    This simple function receives the stat with the name and a message
    """
    return [stats_format(name_stats(catalogue[card_name]), f"These are the stats for {card_name}"), card_name]


def edit_card(card_name):
    pass


results = search_card(easygui.choicebox("What want search?", choices=(catalogue.keys())))
if easygui.ynbox(f"{results[0]}\n Do you wish to edit this card?"):
    edit_card(results[1])
