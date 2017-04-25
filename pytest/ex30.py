people = 30
cars = 40
trucks = 15

if cars >people:
	""" 40>30 true"""
	print("We shoule take the cars.")
elif people > cars:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if trucks > cars:
	print("That's too many trucks.")
	"""15>40 not this way"""
elif trucks < cars:
	print("Maybe we could take the trucks.")
	""" this way"""
else:
	print("We still can't decide.")
if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")

