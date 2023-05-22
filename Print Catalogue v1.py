"""
This is version 1 of print catalogue.
This function will ask the user how they want to format the catalogue and then return that string in
the desired location.
"""
import easygui


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
    return formatted_string + "\n"


def name_stats(values):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(template.keys())
    new_stats = dict(zip(stat_names, values))
    return new_stats


def print_catalogue(format_as, output_location):
    print_string = ""
    if format_as == "As python dictionary":
        print_string = catalogue
    else:  # In bullet points
        for card in catalogue:
            print_string += f"{stats_format(name_stats(catalogue[card]), card)}\n"
    if output_location == "on Here":
        easygui.msgbox(print_string)
        print(print_string)
    else:  # to the terminal
        print(print_string)


format_option = easygui.buttonbox("How do you want to format the list?",
                                  choices=["As python dictionary", "As formatted list"])
output_option = easygui.buttonbox("Where should this be output to?",
                                  choices=["on Here", "to Terminal"])
print_catalogue(format_option, output_option)
