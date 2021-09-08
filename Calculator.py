# Calculator

print("   ***********Welcome To Praddyumns Calculator*********** \n")
num1 = int(input("Enter The First Number Which Do You Want To Exepress Mathamatical Operations \n:>"))
num2 = int(input("Enter The First Number Which Do You Want To Exepress Mathamatical Operations \n:>"))
Calculator = input('''What Do You Want To Do With These Numbers
	1.Add
	2.Substract
	3.Multiply
	4.Divide\n:>''')
if Calculator == "1":
	print(f"The Sum of {num1} and {num2} is Equal To {num1+num2}")
elif Calculator == "2":
	print(f"The Difference Between {num1} and {num2} is Equal To {num1-num2}")
elif Calculator == "3":
	print(f"The Product of {num1} and {num2} is Equal To {num1*num2}")
else:
	print(f"The Quiotient of {num1} and {num2} is Equal To {num1/num2}")
print()
print("**********Thanks For using Praddyumns Calculators**********")