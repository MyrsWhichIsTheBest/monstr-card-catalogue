"""
This is version 1 of my Add Card Function in python
This function asks the user for the name of the new card and asks for the stats of that card too.
"""

import easygui


def add_card():

    stat_names = ["Strength", "Speed", "Stealth", "Cunning"]
    name = easygui.enterbox("What is the name of the new card?")  # ask for the name of the new card
    while True:  # loops until every entry in stats are ints
        stats = easygui.multenterbox(f"Input the stats for {name}:\n"
                                     f"Note: The number must be between 1 and 25", fields=stat_names)
        # asks for the stats of the card
        for i in range(len(stats)):
            stats[i] = int(stats[i])  # replaces the number to an integer
        if type(stats[-1]) is int:
            # if the last number in the stats list is an int it continues the program
            break
    return """
    You successfully created a New Monster Card!\n
    \t
    """


add_card()
