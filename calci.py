class Calculator():

	name = None
	
	def __init__(self,name):
		self.name = name
	
	def add(self,a,b):
		result = a+b
		return result

	def sub(self,a,b):
		result = a-b
		return result

	def mul(self,a,b):
		result = a*b
		return result

	def div(self,a,b):
		result = a/b
		return result


obj1 = Calculator("name1")
a = int(input("Enter the first num"))
b = int(input("Enter the second num"))
print(obj1.add(a,b))
print(obj1.sub(a,b))
print(obj1.mul(a,b))
print(obj1.div(a,b))

