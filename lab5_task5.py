class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "The Points are ({},{})".format(self.x,self.y)

	def add(self,other):
		print (self.x+other.x,self.y+other.y)


p1=Point(10,20)
p2=Point(30,20)
print(p1)
print(p2)
p1.add(p2)
