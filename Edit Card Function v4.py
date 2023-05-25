"""
This is v4 of edit card function, which, in conjunction with search card, will edit the stats of cards
in the catalogue.
This is the trialling version of edit card function.
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
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def number_check(variable):  # this function is used in add card function to check if stats are ints
    """
    This function takes a variable and checks if the variable can be an int
    And will return true or false.
    """
    try:
        int(variable)
    except:
        return False
    else:
        return True


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
    return [stats_format(name_stats(catalogue[card_name]), f"These are the stats for {card_name}"), card_name]


def edit_card(card_name):
    """
    This function will receive a name and will let the user edit the card
    """
    new_list = []
    original_stat = catalogue[card_name]

    while True:
        continue_program = True

        for i in list(template.keys()):
            stat = easygui.integerbox(f"Input the {i} stat for {card_name}:\n"
                                      f"Note: The number must be between 1 and 25",
                                      lowerbound=1, upperbound=25)
            if stat is None:
                continue_program = False
                break
            else:
                new_list.append(stat)

        if continue_program:
            if easygui.ynbox(f"Is this correct?\n"
                             f"{stats_format(name_stats(new_list))}"):
                break
    return [card_name, new_list]


while True:
    results = search_card(easygui.choicebox("What want search?", choices=(catalogue.keys())))
    if easygui.ynbox(f"{results[0]}\n\n Do you wish to edit this card?"):
        edit = edit_card(results[1])
        catalogue[edit[0]] = edit[1]
