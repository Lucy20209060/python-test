# 类
class Dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def sayName(self):
		print('my name is '+self.name)


mydog = Dog('lucy',20)
mydog.sayName()