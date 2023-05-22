"""
This is my v14 of Monster Card Catalogue
I have added print catalogue v2 in place of the placeholder code
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
    return formatted_string + "\n"


def name_stats(values):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(template.keys())
    new_stats = dict(zip(stat_names, values))
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
        stats = easygui.multenterbox(f"Input the stats for {card_name}:\n"
                                     f"Note: The number must be between 1 and 25",
                                     fields=(list(template.keys())), values=original_stat)
        if stats is None:
            return
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
                    new_list.append(stats[i])

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
    return [card_name, new_list]


def delete_card(card_name):
    """
    this function will delete the given card
    """
    if easygui.ynbox(f"Are you sure you want to delete {card_name}?"):
        catalogue.pop(card_name)
        easygui.msgbox(f"You have successfully deleted {card_name}!")


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
    request = easygui.buttonbox("What would you like to do today?",
                                choices=["Add", "Search and Edit", "Delete", "Print", "Exit"])
    if request == "Add":
        user_input = easygui.enterbox("What is the name of the new card?")
        if user_input is None:
            continue
        output = add_card(user_input, template)
        # format dictionary to print out
        catalogue.update({output[0]: list(output[1].values())})
        easygui.msgbox(stats_format(output[1], f"You successfully created a New Monster Card: {output[0]}"))
        # output is the return of the add_card() function which returns the stats and the name
    elif request == "Search and Edit":
        user_input = easygui.choicebox("What want search?", choices=(catalogue.keys()))
        if user_input is None:
            continue
        results = search_card(user_input)
        if easygui.ynbox(f"{results[0]}\n\n Do you wish to edit this card?"):
            edit = edit_card(results[1])
            if edit is None:
                continue
            catalogue[edit[0]] = edit[1]
    elif request == "Delete":
        user_input = easygui.choicebox("What do you want to delete?", choices=list(catalogue.keys()))
        if user_input is None:
            continue
        if len(catalogue) == 2:
            easygui.msgbox("You must have at least 2 cards in your catalogue!")
            continue
        delete_card(user_input)
    elif request == "Print":
        format_option = easygui.buttonbox("How do you want to format the list?",
                                          choices=["As python dictionary", "As formatted list", "Cancel"])
        if format_option == "Cancel":
            pass  # would be 'continue' in main
        output_option = easygui.buttonbox("Where should this be output to?",
                                          choices=["on Here", "to Terminal", "Cancel"])
        if format_option == "Cancel":
            pass  # would be 'continue' in main
        print_catalogue(format_option, output_option)
    else:
        if easygui.ynbox("Do you wish to exit?"):
            easygui.msgbox(f"Goodbye, {exit_catalogue()}!")
            exit()
