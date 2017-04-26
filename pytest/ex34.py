#animals game
from sys import argv
script, infile = argv

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print( "animals:", animals)
print(" let's play a game? guess what kind of animal you choose!")

current_file = open(infile)
question = current_file.readline()

while question:
	print("""\n\t==========================
	animals: %s
	The question is : %s
	============================""" % (animals,question))
	
	print("which place question want to print?")
	pl = input('<')
	
	answer = input('your answer is: >')
	print("your answer is %r" % answer)

	if answer == animals [int(pl)]:
		print("##############right!#####################\n continue?")
		input('>')
	else:
		print("~~~~~~~~~~~~~~sorry!~~~~~~~~~~~~~~~~~~~~~\n")
		input('>')
	
	question = current_file.readline()

current_file.close()
print("That's all! THANKS!")
