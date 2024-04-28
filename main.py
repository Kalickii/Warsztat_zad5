import re

def dice(code):
    dice_types = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    try:
        found_dice = re.findall(r"D\d+", code)

        valid_dice = [dice for dice in found_dice if dice in dice_types]

        throws = [re.findall(r"\d+", code)[0]]

        modifier = int(re.findall(r"\d+", code)[2])
        if "-" in code:
            modifier *= -1
    except IndexError:
        print("Invalid code")
    except TypeError:
        print("Invalid code")
