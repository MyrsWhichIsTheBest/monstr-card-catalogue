"""
This is v1 of the Name Stats function which will be an integral part of the search card function
This will receive a list which will return a dictionary with the stats names as their keys
"""

template = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}


def name_stats(values):
    """
    This function receives the values and returns a dictionary with the stat names as the key
    and values of the stats as the value.
    """
    stat_names = list(template.keys())
    new_stats = template
    for stat in stat_names:
        new_stats[stat] = values[list(new_stats.keys()).index(stat)]
    return new_stats


print(name_stats([17, 19, 3, 2]))
