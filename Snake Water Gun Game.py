# Project = 1
# Snake Water Gun Game 
def snake_water_gun_game():
    import random


    print("Computor's Turn : Snake(s) , Water(w) , Gun(g)")
    RandomNumber = random.randint(1 , 3)
    if RandomNumber == 1:
        ComputersChoice = "s"
    elif RandomNumber == 2:
        ComputersChoice = "w"
    else:
        ComputersChoice = "g" 


    UsersChoice = input("Your Turn : Snake(s) , Water(w) , Gun(g)\n:>")



    def GameWinner(ComputersChoice,UsersChoice):
        if ComputersChoice == "s":
            if UsersChoice == "w":
                return False
            elif UsersChoice == "s":
                return None
            elif UsersChoice == "g":
                return True
        elif ComputersChoice == "w":
            if UsersChoice == "g":
                return False
            elif UsersChoice == "w":
                return None
            elif UsersChoice == "s":
                return True
        else:
            if UsersChoice == "s":
                return False
            elif UsersChoice == "g":
                return None
            elif UsersChoice == "w":
                return True



    print(f"Your Choice = {UsersChoice}")
    print(f"Computer's Choice =  {ComputersChoice}")




    a = GameWinner(ComputersChoice,UsersChoice)
    if a:
        print("Congratulations! You Won The Match")
    elif a == None:
        print("Tie! Your and Computer's Choices are Same")
    elif a == False:
        print("Sorry! You Loss The Match")
    print()
    print()
    print()
    print()
    print()
    print("Thanks For Playing Games on Praddyumn Gaming Studio")
    a = int(input("Do You Want to Play This Game Again 0 = No and 1 = Yes: "))
    if a==1:
        snake_water_gun_game()

snake_water_gun_game()