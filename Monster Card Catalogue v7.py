"""
This is my v7 of Monster Card Catalogue
I will be adding my edit card to this (edit this future me)
"""

import easygui
import os


# non core functions
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


def stats_format(dictionary, message=""):
    """
    this function receives a dictionary and a message which will be formatted into a string
    for the user to read.
    """
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def name_stats(values, names_of_stats):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(names_of_stats.keys())
    new_stats = names_of_stats
    for stat in stat_names:
        new_stats[stat] = values[list(new_stats.keys()).index(stat)]
    return new_stats

# core functions


def add_card(name, new_stats):
    """
    This function asks the user for the name of the new card and asks for the stats of that card too.
    """
    while True:  # loops until every entry in stats are ints
        stats = easygui.multenterbox(f"Input the stats for {name}:\n"
                                     f"Note: The number must be between 1 and 25", fields=(list(new_stats.keys())))
        # asks for the stats of the card
        for i in range(len(stats)):
            if number_check(stats[i]):
                stats[i] = int(stats[i])  # replaces the number to an integer
                if stats[i] < 1 or stats[i] > 25:
                    # this checks if position i in the stats list is between 1 and 25
                    # if it is not it will reset the while loop
                    easygui.msgbox("Please only use whole numbers between 1 and 25", ok_button="Ugh Fine...")
                    # error message for numbers not between 1 and 25
                    break
                else:
                    new_stats[list(new_stats.keys())[i]] = stats[i]
            else:
                easygui.msgbox("Please only input whole numbers", ok_button="Ugh Fine...")
                # error message for non-real numbers and also letters
                break
        if isinstance(stats[-1], int):
            # if the last number in the stats list is an int it continues the program
            break
    return [name, new_stats]


def search_card(card_name, stats_with_names):
    """
    This simple function receives the stat with the name and a message
    """
    return stats_format(name_stats(catalogue[card_name], stats_with_names), f"These are the stats for {card_name}")


def delete_card():
    pass


def print_catalogue():
    pass


def exit_catalogue():
    name = os.getlogin().split()
    return name[0]


# variables
# dictionary containing all my data
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


# main
while True:
    request = easygui.choicebox("wip", choices=["add", "search and edit", "delete", "print", "exit"])
    if request == "add":
        output = add_card(easygui.enterbox("What is the name of the new card?"), template)
        # format dictionary to print out
        catalogue.update({output[0]: list(output[1].values())})
        easygui.msgbox(stats_format(output[1], f"You successfully created a New Monster Card: {output[0]}"))
        # output is the return of the add_card() function which returns the stats and the name
    elif request == "search and edit":
        easygui.msgbox(search_card(easygui.choicebox("What want search?", choices=(catalogue.keys())), template))
    elif request == "delete":
        pass
    elif request == "print":
        print(catalogue)
    else:
        easygui.msgbox(f"Goodbye, {exit_catalogue()}!")
        exit()


