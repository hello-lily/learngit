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

current_line = 1
print( " usr for:")

for n  in range(3):
	n += 1
	print_a_line(n, current_file)
#	current_line += 1

print ("current_line:", current_line)
print ("n: %d" %n)
# 3

print (" old way\n")
current_line = 1
rewind(current_file)
#current_file.seek(0)
print_a_line(current_line, current_file)
#1 input_file  test.txt a space, but print \n

#current_line = current_line + 1
current_line += 1
#that ok!
print_a_line(current_line, current_file)
#2 input_file

current_line = current_line + 1
print_a_line(current_line, current_file)
#3 input_file.readline
#what is readline?

