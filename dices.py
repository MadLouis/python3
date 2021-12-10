import random


class Dice:
    def roll(self):
        first_roll = random.randint(1,6)
        second_roll = random.randint(1,6)
        return first_roll,second_roll


dice = Dice()
print(dice.roll())