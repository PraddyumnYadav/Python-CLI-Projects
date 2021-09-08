# Exercise = 1
# Make Your Own Dictionary .
# English To English Dictionary .

def dictionary():
	print("Welcom To Praddyumn's Dictionary.")
	print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	Dictionary = {
		"Dictionary":"a book that contains a list of the words in a language in the order of the alphabet and that tells you what they mean, in the same or another language",
		"Append":"Adds To The End",
		"Immediate":"happening or done without delay",
		"Suddenly":"adjective. happening, coming, made, or done quickly, without warning, or unexpectedly: a sudden attack. occurring without transition from the previous form, state, etc.; abrupt: a sudden turn. impetuous; rash.",
		"List":"tally",
		"Computer":"Common Operating Machine Particularly Used For Trade Education And Reserch .",
		"Acompany":"To Go With",
		"Sepoy":"Indian Solider in British Service .",
		"Screen":"To Make Ceniema",
		"Shin":"to Kick",
		"Shultan":"Muslim Rulers",
		"Screw":"to Fasten a Twisting Nail",
		"Lucky":"having good luck",
		"Mutable":"Can Change",
		"Immutable":"Can Not Change",
		"Tip":"to (cause to) move so that one side is higher than another side:",
		"Loop":"eyelet, noose; wind, curve; intrauterine device; narrow opening",
		"While":"time; period of time; short time; few moments; effort",
		"Programming":"provide with a program (sequence of instructions for a computer), arrange a program for",
		"preference":"favorite; act of giving priority; special fondness",
		"Simultaneously":"concurrently, concomitantly, contemporaneously, at the same time",
		"sod":"Growing Grass in Wet Soil",
		"hoe":"Spade",
		"Wicked":"Bad",
		"Disguised":"Changing Look",
		"Disgracefull":"Vary Bad",
		"Redeculus":"Looking Bad",
		"ash":"material remaining after something is burned; cinders, embers",
		"bloom":"flower; flowering; glow, radiance; pollen",
		"stir":"movement, motion; agitation; excitement, confusion; prison"
	}
	print("These are Some Words give in Praddyumn's Dictionary",Dictionary.keys())
	a = input("Enter a Word\n:>")
	print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("The Defination or Meaning of", a ," is ->\n" , " <\" " ,Dictionary.get(a)," \"> ")
	print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("Thanks for using Praddyumn's Dictionary.")
	a = int(input("Do You Want To Translate Again 1 = Yes and 0 = N0: "))
	if a==1:
		dictionary()

dictionary()