"""
This is version 2 of my delete card function.
I added a confirmation before deletion
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


def delete_card(card_name):
    """
    this function will delete the given card
    """
    if easygui.ynbox(f"Are you sure you want to delete {card_name}?"):
        catalogue.pop(card_name)


delete_card(easygui.choicebox("What do you want to delete?", choices=list(catalogue.keys())))
