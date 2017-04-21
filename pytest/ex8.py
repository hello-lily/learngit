# -*- coding:utf-8 -*-
# I think there are a lot of print exercises...

formatter = "%r %r %r %r"
# I said I don't know why use %r ,there are few %r in the begin of the text!!
# %r for getting debugging information as the representation version of variable

print (formatter % (1,2,3,4))
#what does it want to say??? 1~4 which one?  no!no!  you see the define about formatter four %r...this is a anytype!
print (formatter % ("one", "two", "three", "four"))
#the same question!  a lot of words I want to say...
print (formatter % (True, False, False, True))
print (formatter % (formatter,formatter,formatter,formatter))
print (formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said gioodnight."))
#one time passed, but lose one line!!
#there is a funny thing, the last command  the third str used "",others ''? why?? single-quotes vs double-quotes  print strings in the most efficient way it can,not copy or exactly the way you wrote.
