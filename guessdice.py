import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

class Guess(Dice):
    def guess(self):
        first,second = self.roll()
        if first == second:
            print("Congratulations you guessed the dice!")
        else:
            print("Better luck next time!")
            print("The dice was ",first,",",second)
            
obj = Guess()
print(obj.roll())

       