def add( a, b):
	print("ADDING %d + %d" % (a,b) )
	return a + b
def subtract ( a, b):
	print("SUBTRACTING %d - %d" % (a , b))
	return a - b
def multiply ( a, b):
	print("MULTIPLYING %d * %d" % (a,b))
	return a * b
def divide (a, b):
	print("DIVIDING %d / %d" % (a,b))
	return a / b

print(" Let's do some math with just functiions!")

age = add (30,5)
#35
height = subtract (78, 4)
#74
weight = multiply ( 90, 2)
#180
iq = divide (100 ,2 )
#50

#there are some format, i want to try!
# you like what ,use what!

print(" Age: %d \tHeight: %d \tWeight: %d \tIQ: %d" %
	(age, height,weight,iq))

# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add( age, subtract( height, multiply(weight, divide(iq,2))))
#		35+	(	74 -	(180*		25))
n = 35+74-180*25
print(" my result is : ", n)

print ("That becomes: ", what, "Can you do it by hand?")

if n == what:
	print("Ture")
else:
	print("False")
