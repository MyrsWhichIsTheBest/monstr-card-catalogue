"""
This is v1 of the Name Stats function which will be an integral part of the search card function
This will receive a list which will return a dictionary with the stats names as their keys
"""


def name_stats(values):
    new_stats = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
    for stat in template:
        new_stats[stat] = values[list(new_stats.keys()).index(stat)]
    return new_stats


template = ["Strength", "Speed", "Stealth", "Cunning"]

print(name_stats([17, 19, 3, 2]))
