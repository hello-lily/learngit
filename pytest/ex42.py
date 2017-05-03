## Animal is-a object, base type.. i don't know what
class Animal(object):
	print("hi, you are Animal!!!")
	pass
## ?? what is pass....pass means nothin?

class Dog(Animal):
	def __init__(self,name):
		## ？？
		self.name = name
	def say(self):
		
		return "dog"
#'s name is %s\n" %self.name)
##??
class Cat(Animal):
	def __init__(self,name):
		##??
		self.name = name
		print("cat's name is %s\n" %self.name)
##??
class Person(object):
	def __init__(self,name):
		self.name = name
		## Person has-a pet of some kind
		print("person's name is %s\n" %self.name)
		self.pet = None
		
		print("pet of person is name is %s\n" %self.pet)

##??
class Employee(Person):
	def __init__(self,name,salary):
		##?? hmm what is this strange magic?
		print("employee's name is") 
		super(Employee,self).__init__(name)
		##??
		self.salary = salary
		print("salary is %s\n" %self.salary)
##??
class Fish(object):
	pass
	print("this is fish")
##??
class Salmon(Fish):
	pass
##??
class Halibut(Fish):
	pass

## rover is-a Dog
print("rover=Cat(\"Rover\")")
rover = Cat("Rover")

## ??
print("satan = Dog(\"Satan\")")
satan = Dog("Satan")

print("mary = Person(\"Mary\")")
mary = Person("Mary")

print("mary.pet = satan")
mary.pet = satan

print (mary.pet.say)
print(satan)
print("frank = Employee(\"Frank\",120000)")
frank = Employee("Frank",120000)

print("frank.pet = rove")
frank.pet = rover

print(frank.pet)

print("flipper = Fish()")
flipper = Fish()

print("crouse = Salmon()")
crouse = Salmon()

print("harry = Halibut()")
harry = Halibut()
