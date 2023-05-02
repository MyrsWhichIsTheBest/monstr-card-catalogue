"""
This is version 2 of my Add Card Function in python
This function asks the user for the name of the new card and asks for the stats of that card too.
I added error messages into this version
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

    stat_names = ["Strength", "Speed", "Stealth", "Cunning"]
    name = easygui.enterbox("What is the name of the new card?")  # ask for the name of the new card
    while True:  # loops until every entry in stats are ints
        stats = easygui.multenterbox(f"Input the stats for {name}:\n"
                                     f"Note: The number must be between 1 and 25", fields=stat_names)
        # asks for the stats of the card
        for i in range(len(stats)):
            if number_check(stats[i]):  # checks if the number in pos 'i' is an int
                if 25 < int(stats[i]) < 1:
                    easygui.msgbox("Please only use whole numbers between 1 and 25", ok_button="Ugh Fine...")
                    # error message
                    break
                stats[i] = int(stats[i])  # replaces the number to an integer
                print("gls")
            else:
                easygui.msgbox("Please only use whole numbers between 1 and 25", ok_button="Ugh Fine...")
                # error message
                break
        if type(stats[-1]) is int:
            # if the last number in the stats list is an int it continues the program
            break
    return """
    You successfully created a New Monster Card!\n
    \t
    """


print(add_card())
