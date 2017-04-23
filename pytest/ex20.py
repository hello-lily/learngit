# functions and files exercise 20

from sys import argv

script, input_file = argv

def print_all ( f ):
	print (f.read())
#3  i know i miss () behind print
#2  there is something wrong about f
#1  print file , no space between name and ( ,this is wrong! there ia a space ,ti's ok!

def rewind(f):
	f.seek(0)

# print what?
#read the x line
def reseek(f,x):
	n = 0
	f.seek(n)
	for i in range(x-1):	
		indata = f.readline()
		n += len(indata)
		f.seek(n)
	return n

def print_a_line(line_count, f):
	print (line_count,"%s" % f.readline())

#add line number and line contex

current_file = open(input_file)

#input_file as input as you do

print ("First let's print the whole file: \n")

print_all(current_file)
#input_file.read()
#current_file.read()

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)
#seek means print ever line!
# define seek from 0

#print seek  ?? what is seek?
#answer:  print test.txt
print ("Let's print three line:")

print( " usr for:")

for n  in range(3):
	n += 1
	print_a_line(n, current_file)

print ("n:", n)

#rewind(current_file)
def printline():
	x = int(input("which line do you want to see: >"))
	n = reseek(current_file,x)
	print ("seek %d line, the charaters is  %d" %(x,n))
	print ("The result is :", x , current_file.readline())

# first do
printline()

def askquestion():
	print ("do you want to try most?")
	print ("RETURE for contiue, CTRL -C for cancel!")
	input (">")
	return True

while askquestion():
	printline()
#        askquestion()

# don't print from line3? why?
# I was wrong, seek(3) used, begin from the third char
# so if I want to begin from the second line , I will math the first line
# how to add the first line?
# 1\ calculate first line's char
# 2\ because the begin number is 0
#    so the calculated result is the next line begin
# 3\ seek from the number, then print!
# def reseek()

#1 input_file  test.txt a space, but print \n

print (" old way\n")
rewind(current_file)
current_line = 1
print_a_line(current_line, current_file)
#that ok!
current_line += 1
print_a_line(current_line, current_file)
#2 input_file

current_line = current_line + 1
print_a_line(current_line, current_file)
#3 input_file.readline
#what is readline?

current_file.close()
