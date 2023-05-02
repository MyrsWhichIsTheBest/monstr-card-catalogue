"""
This is my v2 of Monster Card Catalogue
I have added my catalogue and int checker from a previous project
"""

import easygui


# functions
def int_check(variable):
    """
    This function takes a variable and checks if the variable is an INT
    And will return true or false.
    """
    if type(variable) is int:
        return True
    else:
        return False


def add_card():
    """
    This function asks the user for the name of the new card and asks for the stats of that card too.
    """
    stat_names = ["Strength", "Speed", "Stealth", "Cunning"]
    name = easygui.enterbox("What is the name of the new card?")
    stats = easygui.multenterbox(f"Input the stats for {name}:", stat_names)


def search_edit_card():
    pass


def delete_card():
    pass


def print_catalogue():
    pass


def exit_catalogue():
    pass


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

choices = {
    'Add': add_card,
    'Search/Edit': search_edit_card,
    'Delete': delete_card,
    'Print Catalogue': print_catalogue,
    'Exit': exit_catalogue
}


while True:
    request = easygui.choicebox("What do you want to do?", choices=list(choices.keys()))
    if request:
        easygui.msgbox(choices[request]())
    else:
        break




