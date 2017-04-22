from sys import argv
from os.path import exists

#new stuff os.path ? exists?

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

#we could do these two on one line, how?  rename or copy? 

in_file = open(from_file)
indata = in_file.read()    #indata=from_file

print ("The input file is %d bytes long" % len(indata))  #indata bytes

print ("Does the output file exist?  %r" % exists(to_file))  
#wheather new file exist?
#yes,exists returns True if the file exists
#no, False if not exists
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()   #usrer choose

out_file = open(to_file, 'w')   #to_file to copy
out_file.write(indata)

print ("Alright, all done.")

out_file.close()
in_file.close()
