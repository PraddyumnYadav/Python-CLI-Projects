# In This Programm We Will Make an English Aadhar Card .
# Taking Details .

print("--------------------------------------------------------------------------------")

name = input("Enter Your Name :")
dob = input ("Enter Your Date of Birth :")
gender = input('''Enter Your Gender 
	1. Male
	2. Female\n''')
f_name = input("Enter Your Father's/Husband's Name :")

address = input ("Enter Your Address :")

print("--------------------------------------------------------------------------------")
print("Here is Your Aadhar Card")
print("--------------------------------------------------------------------------------")


print("Name = " ,name)
print("D.O.B = " , dob)
if gender == "1":
	print("Gender = Male")

else :
	print("Gender = Female")

print("Father's/Husband's Name = Mr." , f_name)
print("Address = " , address)