from sys import argv

#agrv? arguments? what's that?

script, first, second, third = argv

print ("The script is called:", script)
print ("You first variable is : ",first)
print ("Your second variable is: ",second)
print ("Your third variable is: ",third)

#maybe pint() comma "," is mistake! don't care about that , is right!

#this is magic script
#1st  $ python3 ex13.py
#Traceback (most recent call last):
#  File "ex13.py", line 5, in <module>
#    script, first, second, third = argv
#ValueError: not enough values to unpack (expected 4, got 1)
# expect 4 para? argv is a modules??four things like argv
#agrv=agrument variable

#2nd
#put 4 parameters 1\ ex13.py 2\ first 3\ 2nd 4\ 3rd
#you can see! each variables  match with the parameter
#$ python3 ex13.py first 2nd 3rd
#The script is called: ex13.py
#You first variable is :  first
#Your second variable is:  2nd
#Your third variable is:  3rd

#3rd
# different py2 py3 print with "()"
#$ python ex13.py stuff things that
#('The script is called:', 'ex13.py')
#('You first variable is : ', 'stuff')
#('Your second variable is: ', 'things')
#('Your third variable is: ', 'that')

#4th
#$ python3 ex13.py stuff things that
#The script is called: ex13.py
#You first variable is :  stuff
#Your second variable is:  things
#Your third variable is:  that

#it's funny!
