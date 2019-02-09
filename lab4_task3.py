import string
def fun():
  d=dict()
  count=0
  list1=[]
  fin=open("58782-0.txt","r")
  punct=string.punctuation
  for words in fin:
    words=words.strip()
    words=words.replace(" ","")
    for i in punct:
      words=words.replace(i,"")
    words=words.lower()
    print(words)
    if words not in d:
      d[words]=1
    else:
      d[words]=d[words]+1
  print ("occurence os the words in book:",d)
  for c in d:
    count=count+1
  print("total no of words in book:",count)
  for key,value in d.items():
    if value==20:
      print("words occuring with more than 20 occurences are:",key)

fun()
   
