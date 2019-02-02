import string
def fun(listofwords):
  d=dict()
  count=0
  list1=[]
  list2=[]
  fin1=open(listofwords,"r")
  fin=open("words.txt","r")
  punct=string.punctuation
  for words in fin:
    words=words.strip()
    words=words.replace(" ","")
    for i in punct:
      words=words.replace(i,"")
    words=words.lower()
    
    if words not in d:
      d[words]=1
    else:
      d[words]=d[words]+1
  print(d)
  for words in fin1:
    words=words.strip()
    words=words.replace(" ","")
    

    list2.append(words)
  print(list2)

  for key,value in d.items():
    if key not in list2:
      print("words not present are:",key)



a=input("enter the name of file of words:")
fun(a)
   
