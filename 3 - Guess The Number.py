def guess_the_Number():
	import random

	divison_line = "----------------------------------------------------------------------------------------------------------"

	print("You Can Not Guess Number More Than 10 Times .")
	a = 0
	n = random.randint(1,500)
	while a<=9:
		a = a+1
		Guess_number = int(input("Guess and Enter a Number.\n:>"))
		if Guess_number<n :
			print("You Guessed to Smaller Number Please Enter a Larger Number.")
			print(divison_line)
		elif Guess_number>n:
			print("You Guessed to Larger Number Please Enter a Smaller Number.")
			print(divison_line)
		else:
			print("Congratulations You Won the Game",a,"Times")
			print(divison_line)
			break
		
	if a>9:
		print("Game Over")
		print(divison_line)

	a = int(input("Do You Want to Play again if Yes enter 1 and if no enter 0 :  "))
	if a==1:
		guess_the_Number()

guess_the_Number()