import os
import random
import time

enemy = {
    "name": "Enemy",
    "health": 100
}

player = {
    "health": 100,
}

enemyActions = ["Attack", "Heal", "Heal", "Attack", "Attack", "Attack"]
playerActions = ["Attack", "Heal"]

clear = lambda: os.system('cls')

clear()

print("Enemy Health: " + str(enemy["health"]) + "\nYour Health: " + str(player["health"]))

def playerAction():
    action = input("1: " + playerActions[0] + " 2: " + playerActions[1] + "\n")

    if (action == "1"):
        enemy["health"] -= 10
    elif (action == "2"):
        player["health"] += 15
    else:
        print("You did not enter 1 or 2!")
    
    clear()
    
    print("Enemy Health: " + str(enemy["health"]) + "\nYour Health: " + str(player["health"]))

def enemyAction():
    action = enemyActions[random.randrange(0, len(enemyActions))]
    clear()
    print(enemy["name"] + " uses " + action)
    time.sleep(1.5)

    if (action == enemyActions[0]):
        player["health"] -= 10
    elif (action == enemyActions[1]):
        enemy["health"] += 15

    print("Enemy Health: " + str(enemy["health"]) + "\nYour Health: " + str(player["health"]))

while enemy["health"] > 0 and player["health"] > 0:
    playerAction()
    enemyAction()
else:
    if (enemy["health"] <= 0):
        print("You win!")
    else:
        clear()
        print("You have been defeated!")