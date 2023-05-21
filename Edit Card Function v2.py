"""
This is v2 of edit card function, which, in conjunction with search card, will edit the stats of cards
in the catalogue.
I made the default stats the original stats and made the edit prompt more user-friendly.
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
    """
    This function will receive a name and will let the user edit the card
    """
    list_empty = []
    original_stat = catalogue[card_name]
    while True:
        continue_program = True
        stats = easygui.multenterbox(f"Input the stats for {card_name}:\n"
                                     f"Note: The number must be between 1 and 25",
                                     fields=(list(template.keys())), values=original_stat)
        for i in range(len(stats)):
            if number_check(stats[i]):
                stats[i] = int(stats[i])  # replaces the number to an integer
                if stats[i] < 1 or stats[i] > 25:
                    # this checks if position i in the stats list is between 1 and 25
                    # if it is not it will reset the while loop
                    easygui.msgbox("Please only use whole numbers between 1 and 25", ok_button="Ugh Fine...")
                    # error message for numbers not between 1 and 25
                    stats = original_stat
                    continue_program = False
                    break
                else:
                    list_empty.append(stats[i])

            else:
                easygui.msgbox("Please only input whole numbers", ok_button="Ugh Fine...")
                # error message for letters
                stats = original_stat
                continue_program = False
                break
        if continue_program:
            if easygui.ynbox(f"Is this correct?\n"
                             f"{stats_format(name_stats(stats))}"):
                break
    return [card_name, list_empty]


while True:
    results = search_card(easygui.choicebox("What want search?", choices=(catalogue.keys())))
    if easygui.ynbox(f"{results[0]}\n Do you wish to edit this card?"):
        edit = edit_card(results[1])
        catalogue[edit[0]] = edit[1]
