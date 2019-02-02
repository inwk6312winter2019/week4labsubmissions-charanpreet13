def fun(pattern,replacement,file1,file2):
  try:
   fin1=open(file1,"r")
   fin2=open(file2,"w")
   for word in fin1:
     if word==pattern:
       
       word=word.replace(pattern,replacement)
     
     fin2.write(word)
     
   print("file copying was successful")
   
   return fin2
  
  except:
    print("file copying was unsuccessful")

  










x=input("enter pattern string: ")
y=input("enter replacement string: ")
a=input("enter file1 name: ")
b=input("enter file2 name: ")
print(fun(x,y,a,b))
