"""
This is version 3 of my Add Card Function in python
This function asks the user for the name of the new card and asks for the stats of that card too.
I fixed bugs
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


def add_card():
    new_stats = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
    stat_names = ["Strength", "Speed", "Stealth", "Cunning"]
    name = easygui.enterbox("What is the name of the new card?")  # ask for the name of the new card
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
                    # error message
                    break
                else:
                    new_stats[stat_names[i]] = stats[i]
            else:
                easygui.msgbox("Please only use whole numbers between 1 and 25", ok_button="Ugh Fine...")
                # error message
                break
        if type(stats[-1]) is int:
            # if the last number in the stats list is an int it continues the program
            break
    return new_stats


print(add_card())
