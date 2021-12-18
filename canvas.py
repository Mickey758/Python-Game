from variables import player, food
def update():
    y = '\n' * player.y
    x = '  ' * player.x
    y2 = '\n' * food.y
    x2 = '  ' * food.x
    if player.x > food.x:
        print(f"{y}{x}O",end="")
        print("\x1b[0;0H",end="")
        print(f"{y2}{x2}X",end="")
    else:
        print(f"{y2}{x2}X",end="")
        print("\x1b[0;0H",end="")
        print(f"{y}{x}O",end="")
    print("\x1b[0;0H",end="\r")