from .dice_model import Dice
from bmodules.constants import D
import re


class DiceManager:
    def __init__(self, args):
        """
        Manages the users input and rolls the amount of dice requested.
        """
        self.error = False
        die = "".join(args)

        if re.search("[1-9]d[1-9]", die) is None:
            raise NameError("Invalid Dice")
        self.d_one = Dice(die.split(D))

    def combine(self, results: list):
        """
        combines the dice results into one total

        Args:
            ds (list): a list of all dice rolled

        Returns:
            total (int): the total of all the dice rolled.
        """
        total = 0
        for dice in results:
            total += int(dice)
        return total

    def print_result(self):
        """
        Prints the results of the rolled dice.

        Returns:
            (str): the results of the roll in string form
        """
        results = self.d_one.roll_dice()
        return f"```ini\n{results} Total: {self.combine(results)}\n```"
