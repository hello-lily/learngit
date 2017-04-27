# class test  add parameter self
# test() takes 1 positional argument but 2 were given, 2 given self and para
class Thing:
	def test(self,message):
		print("%s"% message)

a = Thing()
a.test("hello world")

ten_things ="Apples Oranges Crows Telephone Light Sugar"
print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
# string into list with ' ' 
more_stuff = ["Day", "Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
#from Day, add to stuff
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(stuff)
	print("There are %d items now." % len(stuff))

print ("There we go: ",stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop())
print (' '.join(stuff[0:5]))
#print (stuff)
print ('#'.join(stuff[3:6]))
