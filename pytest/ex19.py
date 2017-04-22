def cheese_and_cracker (cheese_count, boxes_of_crackers):
	print ("You have %d cheeses!" % cheese_count)
	print ("You have %d boxes of crackers!" % boxes_of_crackers)
	print ("Man that's enough for a party!")
	print ("Get a blanket. \n")

print ("We can just give the function numbers directly:")
cheese_and_cracker (20, 30)
# space name (
# don't care about that, it's ok!

print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_cracker(amount_of_cheese, amount_of_crackers)


print ("We can even do math inside too:")
cheese_and_cracker(10 + 20, 5 + 6)

print ("And we can combine the two, variables and math:")
cheese_and_cracker(amount_of_cheese + 100, amount_of_crackers + 1000)

#add new functon
print (" Can use %  or /?")
cheese_and_cracker (amount_of_cheese % 3 ,20/5)
#1 and 4 right!

#print (" strint?")
#cheese_and_cracker ( int(a), int("ab"))
# int not str
#   NameError: name 'a' is not defined
