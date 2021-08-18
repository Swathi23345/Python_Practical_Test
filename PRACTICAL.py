class Heroes:     # initializing heroes class
    heroes = input("Enter the strengths of heroes(include spaces between each of them): ")
    for x in list(heroes):
        if x not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '):
            raise Exception("Delimiter error: check if entered string contains only numerals n spaces")
    heroes_strength = list(map(int, heroes.split(" ")))
    heroes_strength.sort()
    list1 = heroes_strength


class Enemies:      # initiating enemies class
    enemies = input("Enter the strengths of enemies(include spaces between each of them): ")
    for x in list(enemies):
        if x not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '):
            raise Exception("Delimiter error: check if entered string contains only numerals n spaces")
    enemies_strength = list(map(int, enemies.split(" ")))
    enemies_strength.sort()
    list2 = enemies_strength


if(len(Heroes.list1) != len(Enemies.list2)):
    raise Exception("Inequality in number of heroes and enemies. Please make sure equal number of participants")


def compareStrengths(list1, list2):  # defining a function for comparing the strengths
    if (sorted(list1) == sorted(list2)):
        print("Both heroes and enemies have same strengths!")
    else:
        dummy = []
        for a in range(0, len(Heroes.list1)):
            if (list1[a] >= list2[a]):
                dummy.append("Heroes Won")
            else:
                dummy.append("Enemies won")
        if "Enemies won" in dummy:
            print("RESULT: LOSE")
        else:
            print("RESULT: WIN")


compareStrengths(Heroes.list1, Enemies.list2)

