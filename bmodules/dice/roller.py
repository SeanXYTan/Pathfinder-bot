from .dice_model import Dice
from bmodules.constants import D 
from bmodules.exceptions import DiceError, ModError
import re


class DiceManager:
    def __init__(self, *args):
        """
        Manages the users input and rolls the amount of dice requested.
        1 = dice (1d20)
        2 = dice with modifier (1d20+3)
        3 = dice with modifier dice (1d20+3d4)
        """
        die = "".join(args[0])
        self.symbol = re.findall("[+\-\*\/]", die)

        def dice_check(die):
            if re.search("[1-9]d[1-9]", die) is None:
                raise DiceError("Invalid Dice")
        
        if len(self.symbol) > 0:
            if re.search(f"{self.symbol}[1-9]", die) is None:
                raise ModError("Invalid Mod")
            sep = die.split(self.symbol[0])

            dice_check(sep[0])
            self.d_one = Dice(sep[0].split(D))

            if re.search("[1-9]d[1-9]", sep[1]) is not None:
                self.d_two = Dice(sep[1].split(D))
                self.eg = 3
            else:
                self.mod = sep[1]
                self.eg = 2

        else:
            dice_check(die)
            self.d_one = Dice(die.split(D))
            self.eg = 1


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
        if self.eg == 1:
            results = self.d_one.roll_dice()
            return f"```ini\n{results} \nTotal: {self.combine(results)}\n```"
        
        if self.eg == 2:
            results = self.d_one.roll_dice()
            total = str(self.combine(results)) + self.symbol[0] + str(self.mod)
            return f"```ini\n{results}{self.symbol[0]}{self.mod} \nTotal: {eval(total)}\n```"
        
        if self.eg == 3:
            results1 = self.d_one.roll_dice()
            results2 = self.d_two.roll_dice()
            total = str(self.combine(results1)) + self.symbol[0] + str(self.combine(results2))
            return f"```ini\n{results1}+{results2} \nTotal: {eval(total)}\n```"
