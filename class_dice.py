import random
class Dice:
    def roll(self):
        rolling = (random.randint(1, 6), random.randint(1, 6))
        return rolling


throw = Dice()
print(throw.roll())