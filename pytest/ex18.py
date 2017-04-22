# this one is like your scripts with argv
def print_two ( *args):
	arg1,arg2 =args
	print ("arg1: %r, arg2: %r" % (arg1, arg2))

#ok, that *args is actually pointless, we can just do this
# so what is*args?   means a lot of strings

def print_two_again(arg1, arg2):
	print ("arg1: %s, arg2: %s" % (arg1, arg2))
# %r  there is ' with the word ;
# %s  only the word you want to print

#this just takes one argument
def print_one(arg1):
	print ("arg1: %r" % arg1)
#replace % use , ; 
#" ," means and  ; 
#"% " means replace

#this one takes no arguments
def print_none():
	print ("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
