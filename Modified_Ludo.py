# Modified Ludo
def Modified_Ludo():
    import random
    c = random.randint(1,6)
    b = random.randint(1,6)
    print(f'''Computers Turn :>
    {c}''')
    a = int(input("Your Turn 1 = Spin and 2 = Do not spin (if you don't spin you will loss) : "))
    if a==1:
        print(b)
    else:
        print("You Loss")

    if c>=b:
        print("You loss")
    elif b>=c:
        print("You Win")
    else:
        print("Your and Computers Numbers are Same")
    
    a = int(input("Do You Want To Play again 1 = Yes and 0 = No : "))
    if a==1:
        Modified_Ludo()

Modified_Ludo()