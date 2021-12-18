import random
import os
clear = lambda: os.system("cls")
class player:
    x = 30
    y = 15
class food:
    x = 30
    y = 15
    @staticmethod
    def spawn():
        food.x = random.randint(0,59)
        food.y = random.randint(0,29)
class progress:
    score = 0