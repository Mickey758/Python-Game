from variables import clear, food
from canvas import update
import game
import time
import keyboard
import os

os.system('mode 120,30')
food.spawn()
game.title()
while True:
    clear()
    update()    
    key = keyboard.read_key()
    game.update(key)
    time.sleep(0.05)
    game.title()
    clear()