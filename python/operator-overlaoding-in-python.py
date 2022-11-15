# Python Program illustrate how
# to overload an binary + operator
# And how it actually works

class A:
	def __init__(vamstar, a):
		vamstar.a = a

	# adding two objects
	def __add__(vamstar, o):
		return vamstar.a + o.a
ob1 = A(4)
ob2 = A(8)
ob3 = A("welcome")
ob4 = A("company")

print(ob1 + ob2)
print(ob3 + ob4)

