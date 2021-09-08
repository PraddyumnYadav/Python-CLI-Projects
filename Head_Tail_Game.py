# HeadTailGame
def HeadTailGame():
    import random
    print("Computers Toss the Coin")
    UC = int(input("Guess and Enter Computers Result of Toss 1 = Head and 0 = Tail : "))
    CC = random.randint(0,1)
    if CC==1:
        CC = "Head"
    else:
        CC = "Tail"

    if UC==1:
        UC = "Head"
    else:
        UC = "Tail"

    print(f'''Computer Choice :>
    {CC}''')
    print(f'''Your Choice :>
    {UC}''')


    if UC==CC:
        print("You Win!")
    else:
        print("You Loss!")

    a = int(input("Do You want To Replay The Game 1 = Yes and 0 = No: "))
    if a==1:
        HeadTailGame()

HeadTailGame()