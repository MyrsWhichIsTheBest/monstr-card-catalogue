"""
This is v3 of the Name Stats function which will be an integral part of the search card function
This will receive a list which will return a dictionary with the stats names as their keys
I used the zip() function to avoid using a for loop unnecessarily
"""

template = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}


def name_stats(values):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(template.keys())
    new_stats = dict(zip(stat_names, values))
    return new_stats


print(name_stats([17, 19, 3, 2]))
