# Snake Water Gun
import random

manPoint = 0
compPoint = 0
noofChances = 0
Tie = 0

for noofChances in range(10):

    # Input Section
    lst = ["Snake" , "Water" , "Gun"]
    comp = random.choice(lst)
    man = input("Please Enter s = Snake , w = Water , g = Gun : ")
    if man == "s":
        man = "Snake"
    elif man == "w":
        man = "Water"
    else:
        man = "Gun"
    
    # Primary Result Chossing Section
    def gameResult(comp , man):
        if man == "Snake":
            if comp == "Snake":
                return None
            elif comp == "Water":
                return True
            else:
                return False
        elif man == "Water":
            if comp == "Water":
                return None 
            else:
                return True
        else:
            return None

    Result = gameResult(comp , man)

    # Point Section
 
    if Result == True:
        manPoint+=1
        print(f"Computer = {comp} , You = {man} \nSo You Win \n")
    elif Result == False:
        compPoint+=1
        print(f"Computer = {comp} , You = {man} \nSo You Loss \n")
    else:
        Tie+=1
        print(f"Computer = {comp} , You = {man} \nSo This Chance was Tie \n")

# Final Result Section
if manPoint>=compPoint:
    print(f"Computers point = {compPoint} , Tie = {Tie} and Your Point = {manPoint} \n********* So You are Winner of This Match *********")
elif compPoint>=manPoint:
    print(f"Computers point = {compPoint} , Tie = {Tie} and Your Point = {manPoint} \n********* So Computer are Winner of This Match *********")
elif manPoint==compPoint:
    print(f"Computers point = {compPoint} , Tie = {Tie} and Your Point = {manPoint} \n********* So This Match Was Tie *********")
