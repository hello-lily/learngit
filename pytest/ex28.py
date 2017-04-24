from sys import argv

script, input_file = argv

def print_r( str, r):
	print("""
\t-----------------------------	
\tRecord: %s"""% str)
	if eval(str) == r:
		print("\tSmart!\n\t--------------------")
		return True
	elif eval(str)!= r:	
		print("\tSorry!\n\t------------------")		
		return False

def read_line(current_file):
	f=current_file.readline()
	return f

t = True
f = False

current_file = open(input_file)
#current_file.seek(0)

str = read_line(current_file)
while str:
	print ("""\n=========================
QUESTION: 
%sTrue or False?
True hit t; False hit f""" % str)
	i = input(">")
	if i=='t':
		print("you choose yes! ")			
		print_r(str,t)
	else:		
		print("you said no!")
		print_r(str,f)
	str = read_line(current_file)

current_file.close()

