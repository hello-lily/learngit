#1st
#Traceback (most recent call last):
#  File "ex11.py", line 2, in <module>
#    age = raw_input()
#NameError: name 'raw_input' is not defined
#try to add def raw_input()
def raw_input():
	return input()

print ("How old are you?"),
age = raw_input()
#print (age)
print ("How tall are you?"),
height = raw_input()
print ("How much do you weigh?"),
weigh = raw_input()

print ("So, you're %r old, %r tall and %r heavy." %
	 (age, height, weigh))

#I don't know what will print when I add the comma at the end of print comment,
# also don't know what will print when I add /n in the paremeter of the print
#2nd 
#Traceback (most recent call last):
#  File "ex11.py", line 16, in <module>
#    age, height, weight))
#NameError: name 'weight' is not defined
# weith!!!spell wrong....
#3rd
#TypeError: not all arguments converted during string formatting
#delelt /n   not this wrong~ the code wrong i put $ replace %  so...
# thare is a different between python2 and python3 input() as a function replaceraw_input()
# there is different when I input, the example's input on one line, 
# but I input in next line!
