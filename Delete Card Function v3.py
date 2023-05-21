"""
This is version 2 of my delete card function.
I added a confirmation before deletion
"""
import easygui


catalogue = {
    "Stoneling": [7, 1, 25, 15],
    "Shmorby": [1, 6, 21, 19]
}


def delete_card(card_name):
    """
    this function will delete the given card
    """
    if easygui.ynbox(f"Are you sure you want to delete {card_name}?"):
        catalogue.pop(card_name)
        easygui.msgbox(f"You have successfully deleted {card_name}!")


while True:
    if len(catalogue) == 2:
        easygui.msgbox("You must have at least 2 cards in your catalogue!")
        continue
    delete_card(easygui.choicebox("What do you want to delete?", choices=list(catalogue.keys())))
