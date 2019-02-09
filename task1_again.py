import string
def fun():
	fin=open("words.txt","r")
	punct=string.punctuation
	print(punct)	
	for words in fin:
		words=words.strip()
		words=words.replace(" ","")
		for c in punct:
			words=words.replace(c,"")
		words=words.lower()
		print(words)
		
fun()	
