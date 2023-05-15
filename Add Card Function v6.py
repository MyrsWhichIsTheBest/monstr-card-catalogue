"""
This is version 6 of my Add Card Function in python
This function asks the user for the name of the new card and asks for the stats of that card too.
I removed some redundant variables
"""

import easygui


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
    formatted_string = message
    for key, value in dictionary.items():
        formatted_string += f"\n {key}: {value}"
    return formatted_string


def add_card(name):
    """
    This function asks the user for the name of the new card and asks for the stats of that card too.
    """
    new_stats = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
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


output = add_card(easygui.enterbox("What is the name of the new card?"))
# format dictionary to print out
# catalogue.update({output[0]: list(output[1].values())})
# this code above adds the output to the catalogue (aka monster_card_dictionary v1)
easygui.msgbox(stats_format(output[1], f"You successfully created a New Monster Card: {output[0]}"))
# output is the return of the add_card() function which returns the stats and the name
