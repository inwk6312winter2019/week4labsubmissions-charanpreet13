class Kangaroo:
  def __init__(self):
    self.pouch_contents=[]

  def put_in_pouch(self,obj):
      self.pouch_contents.append(obj)

  def __str__(self):
    return ("a string representation of the Kangaroo object"+str(self.pouch_contents))

obj1=Kangaroo()
obj2=Kangaroo()
obj2.pouch_contents.append("hi")
obj1.put_in_pouch(obj2)

for content in obj1.pouch_contents:
  print(content)
