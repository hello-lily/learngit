class Other(object):
	def implicit(self):
		 print("Pa impliciat()")

	def override(self):
		print("Pa override()")

	def altered(self):
	        print ("PARENT altered()")

class Ch(object):
	def __init__(self):
		self.other = Other()
	# adjust other()   i think init will include other()'s def
	def implicit(self):
		self.other.implicit()

	def override(self):
		print("CH override()")

	def altered(self):
		print( "CHILD, BEFORE PARENT altered()")
                #super(Ch, self).altered()
                #no super
		self.other.altered()
		print ("CHILD, AFTER PARENT altered()")


#dad = Pa()

son = Ch()

#dad.implicit()
son.implicit()


#dad.override()
son.override()


#dad.altered()
son.altered()
