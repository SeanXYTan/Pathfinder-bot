# 1d2, 1d3, 1d4, 1d6, 1d10, 1d20, 1d100
from random import randint


class Dice:
    """
    Dice class that handles dice rolling
    """

    def __init__(self, dice: list):
        """
        Args:
            dice (list): Holds both the number of dices and the number of faces of the die.
        Vars:
            num (int): the number of dice being rolled
            face (int): the number of faces each dice has
        """
        self.num = int(dice[0])
        self.face = int(dice[1])

    def roll_dice(self):
        """
        Rolls the dice based on the number of dices.

        Returns:
            dice_rolled (list): the results of the dice rolled
        """
        dice_rolled = []
        for rolls in range(self.num):
            dice_rolled.append(randint(1, self.face))
        return dice_rolled
