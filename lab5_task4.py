class time:
	def __init__(self,time):
		self.t=time
		self.minutes,self.seconds=divmod(time,60)
		self.hours,self.minutes=divmod(self.minutes,60)
		print(self.hours,self.minutes,self.seconds)

	def __str__(self):
		return ('Time= %.2d:%.2d:%.2d')%(self.hours,self.minutes,self.seconds)

	def is_after(self,t1):
		return t1.t>self.t
t1=time(900)
t2=time(1500)

print(t1)
print(t2)
print(t2.is_after(t1))

