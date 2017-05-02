class Y:
	"""father class Y"""
	print("this is X's father Y!")

class X(Y):
	""" Make a class named X that is-a Y"""
	Q = "hi a!"
	def __init__(self):
		J = "hello x's j!"
		Q = "hi this is Q!"
		print(J)
		print("class X has-a __init__that takes self and J parameters.")
	def M(self,J):
		j = J
		print(J)
		print("class X has-a function named M that takes self and J parameters.")
	K = Q
J="hi"
foo = X()
foo.M(J)
print (foo.K)

r'''
result!
1\ first print Y
this is X's father Y!
2\init X
hello x's j!
class X has-a __init__that takes self and J parameters.
3\use foo.M(J)
hi
class X has-a function named M that takes self and J parameters.
4\print foo.k
hi a!
'''	
