## Helth Managment System
## 3 Clients = Harry,Hammad,Rohan

# use This Finction
def getdate():
	import datetime
	return datetime.datetime.now()

 
## Total 6 Files

# 0 = Take Input See Details or Fill Details

# if 0 = Fill Details
# 1 = Take Input Client Name
# 2 = Take Input Record Meal or Exercise
# 3 = Store it in File With getdate

# if 0 = Fill See Details
# 1 = Take Input Client Name
# 2 = Take Input See Meal or Exercise
# 3 = Print getdate + 2



Record_or_See = input('''What Do You Want To Do
	1.See Your Report
	2.Add Details in Your Report
	:>''')
if Record_or_See == "2":
	Client = input('''Enter Client Number
		1.Harry
		2.Rohan
		3.Hammad
	:>''')
	CLient_Activity = input('''Enter Activity Number
		1.Meal
		2.Exercise
	:>''')
	if Client == "1" and CLient_Activity == "1":
		f = open("Harry Meal.txt","a")
		Harry_Meal = input("Enter Your Meal\n:>")
		f.write(f"[{getdate()}] :> {Harry_Meal}\n")
		f.close()
	elif Client == "1" and CLient_Activity == "2":
		f = open("Harry Exercise.txt","a")
		Harry_Exercise = input("Enter Your Exercise\n:>")
		f.write(f"[{getdate()}] :> {Harry_Exercise}\n")
		f.close()
	elif Client == "2" and CLient_Activity == "1":
		f = open("Rohan Meal.txt","a")
		Rohan_Meal = input("Enter Your Meal\n:>")
		f.write(f"[{getdate()}] :> {Rohan_Meal}\n")
		f.close()
	elif Client == "2" and CLient_Activity == "2":
		f = open("Rohan Exercise.txt","a")
		Rohan_Exercise = input("Enter Your Exercise\n:>")
		f.write(f"[{getdate()}] :> {Rohan_Exercise}\n")
		f.close()
	elif Client == "3" and CLient_Activity == "1":
		f = open("Hammad Meal.txt","a")
		Hammad_Meal = input("Enter Your Meal\n:>")
		f.write(f"[{getdate()}] :> {Hammad_Meal}\n")
		f.close()
	elif Client == "3" and CLient_Activity == "2":
		f = open("Hammad Exercise.txt","a")
		Hammad_Exercise = input("Enter Your Exercise\n:>")
		f.write(f"[{getdate()}] :> {Hammad_Exercise}\n")
		f.close()
else:
	Client = input('''Enter Client Number
		1.Harry
		2.Rohan
		3.Hammad
	:>''')
	CLient_Activity = input('''Enter Activity Number
		1.Meal
		2.Exercise
	:>''')
	if Client == "1" and CLient_Activity == "1":
		f = open("Harry Meal.txt")
		content = (f.read())
		print(content)
	elif Client == "1" and CLient_Activity == "2":
		f = open("Harry Exercise.txt")
		content = (f.read())
		print(content)
	elif Client == "2" and CLient_Activity == "1":
		f = open("Rohan Meal.txt")
		content = (f.read())
		print(content)
	elif Client == "2" and CLient_Activity == "2":
		f = open("Rohan Exercise.txt")
		content = (f.read())
		print(content)
	elif Client == "3" and CLient_Activity == "1":
		f = open("Hammad Meal.txt")
		content = (f.read())
		print(content)
	elif Client == "3" and CLient_Activity == "2":
		f = open("Hammad Exercise.txt")
		content = (f.read())
		print(content)
print()
print()
print("Thanks! For Visting Praddyumn Jim Trainer's Jim")