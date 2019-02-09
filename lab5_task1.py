import math
class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def distance_between_point(self,p1,p2):
		print(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2))
p1=(5,10)
p2=(10,15)
p=Point(p1,p2)
p.distance_between_point(p1,p2)
