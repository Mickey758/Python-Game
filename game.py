from variables import player, food, progress
from console.utils import set_title
def title():
    set_title(f"Score = {progress.score}")
def update(key):
    match key:
        case "down":
            player.y += 1 if player.y < 29 else 0
        case "up":
            player.y -= 1 if player.y > 0 else 0
        case "left":
            player.x -= 1 if player.x > 0 else 0
        case "right":
            player.x += 1 if player.x < 59 else 0
    if player.x == food.x and player.y == food.y:
        progress.score += 1
        food.spawn()