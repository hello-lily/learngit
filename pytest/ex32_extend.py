#we can also build lists, first start with an empty one
elements = []
eletest = []
pp = []
qq = []

#then use the range function to do 0 to 5 counts
for i in range(10):
	#range as this?  0-5 the same  range(0,6)
	print("Adding %d to the list." %i)
	#append is a function that lists understand
	# example use append
	elements.append(i)
print(elements)
for i in range(6,10):
	eletest.append(i)
	print("eletest %r " % i)
print(eletest)

# combine two list
elements.__add__(eletest)
print("element add eletest:elements the same",elements)

# find list2 whether in list1
print("element contains eletest?true?",elements.__contains__(eletest))

#delete wrong
#print("pp delete element:",pp.__delitem__(elements))

#don't spport???
#print("element delslice eletest:",elements.__delslice__(eletest))

#eq  ==
print("element eq test?false",elements.__eq__(eletest))
qq = pp
print("pp eq qq?",pp.__eq__(qq))

#qq.__getattribute__('alice')
#qq.alice  what ? why?  not work...

qq = elements.__iadd__(elements)
print("qq iadd elements:",qq)
qq.remove(0)
print("qq remove 0:",qq)
for i in range(1,5):
	qq.remove(i)
print("qq remove 5:",qq)


#print("%s"%elements.count(6))
#now we can print them out too
#for i in elements:
print("Element was: %s" %elements)
print("Eletest was: %s" %eletest)
print("qq: %s" % qq)
print("pp: %s" % pp)
