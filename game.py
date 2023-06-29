tools = {"teeth": {"name": "teeth", "cost": 0, "earnings": 1, "next": "rustyScissors"}, "rustyScissors": { "name": "rusty scissors", "cost": 5, "earnings": 5, "next": "oldMower"}, "oldMower": {"name": "old mower", "cost": 25, "earnings": 50, "next": "newMower"}, "newMower": {"name": "new mower", "cost":250, "earnings": 100, "next": "students"}, "students": {"name": "students", "cost": 500, "earnings": 250, "next": "none"}}


def gameOn():
    wallet = 0
    currentTool = tools["teeth"]
    nextTool = tools.get(currentTool["next"])
    gameOver = False
    while gameOver != True:
        print(f"\n*************\nYou have ${wallet} and you are using your {currentTool['name']} to cut grass for ${currentTool['earnings']}\n*************\n")
        choice = input(f"\n*************\nWould you like to cut a lawn for ${currentTool['earnings']}? y/n: \n*************\n").lower()
        if choice != "y" and choice != "n":
            print("\n*************\nPlease enter y or n\n*************\n")
            continue
        if choice == "y":
            wallet += currentTool['earnings']
        elif choice == "n":
            print("\n*************\nyou make nothing and another day is gone forever...\n*************\n")
            continue
        if wallet >= nextTool["cost"]:
            newTool = input(f"\n*************\n You have earned ${wallet} and can afford {nextTool['name']}, would you like to spend ${nextTool['cost']} to get it? y/n: \n*************\n").lower()
            if newTool == 'y':
                currentTool = nextTool
                nextTool = tools.get(currentTool['next'])
                print(currentTool, nextTool)
            else:
                continue
        if currentTool == tools["students"]:
            print(f"\n*************\nYou've earned ${wallet} and have a fleet of students working for you.\n That's surely enough to retire :)\n*************\n GAME OVER \n*************\n")
            gameOver = True
gameOn()