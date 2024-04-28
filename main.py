import re
from random import randint

def dice(code):
    """
    Dice roll.
    User input, how many throws, which type of dice, and additional modifier he want to use in the simulation.
    :param code: xDy+z  where: x = throws, Dy = type of dice, z = additional modifier ex. '2D10+10'
    :rtype: int
    :return: Function returns simulation of the dice roll.
    """
    dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    throws = 0
    valid_dice = 0
    modifier = 0

    try:
        found_dice = re.findall(r"D\d+", code)[0]
        if found_dice in dice_types:
            valid_dice = int(found_dice[1::])

        if "D" == code[0]:
            throws = 1
        else:
            throws = int(re.findall(r"\d+", code)[0])

        modifier = int(re.findall(r"\d+", code)[-1])
        if "-" in code:
            modifier *= -1
        if "-" not in code and "+" not in code:
            modifier = 0
    except IndexError:
        print("Invalid code")
    except TypeError:
        print("Invalid code")
    result = throws * randint(1, valid_dice) + modifier
    return result
