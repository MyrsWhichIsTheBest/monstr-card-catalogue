"""
This is my v2 of Monster Card Catalogue
I have added my first function, Add Card Function v4, and it's required functions
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


def stats_format(list, message=""):
    formatted_string = message
    for key, value in list.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


# core functions

def add_card(name):
    """
    This function asks the user for the name of the new card and asks for the stats of that card too.
    """
    new_stats = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
    stat_names = ["Strength", "Speed", "Stealth", "Cunning"]
    while True:  # loops until every entry in stats are ints
        stats = easygui.multenterbox(f"Input the stats for {name}:\n"
                                     f"Note: The number must be between 1 and 25", fields=stat_names)
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
                    new_stats[stat_names[i]] = stats[i]
            else:
                easygui.msgbox("Please only input whole numbers", ok_button="Ugh Fine...")
                # error message for non-real numbers and also letters
                break
        if isinstance(stats[-1], int):
            # if the last number in the stats list is an int it continues the program
            break
    return [name, new_stats]


def search_edit_card():
    pass


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


# main
while True:
    request = easygui.choicebox("wip", choices=["add", "search", "delete", "print", "exit"])
    if request == "add":
        output = add_card(easygui.enterbox("What is the name of the new card?"))
        # format dictionary to print out
        catalogue.update({output[0]: list(output[1].values())})
        easygui.msgbox(stats_format(output[1], f"You successfully created a New Monster Card: {output[0]}"))
        # output is the return of the add_card() function which returns the stats and the name
    elif request == "search":
        pass
    elif request == "delete":
        pass
    elif request == "print":
        print(catalogue)
    else:
        easygui.msgbox(f"Goodbye, {exit_catalogue()}!")
        exit()


