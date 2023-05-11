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


def stats_format(dictionary, message=""):
    formatted_string = message
    for key, value in dictionary.list():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def edit_card(query):
    (catalogue[query])


edit_card(easygui.choicebox("wip", choices=(catalogue.keys())))
