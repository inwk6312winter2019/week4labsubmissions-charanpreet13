import string
def fun():
        fin=open("58782-0.txt","r")
        punct=string.punctuation
        print(punct)    
        for words in fin:
                words=words.strip()
                words=words.replace(" ","\n")
                for c in punct:
                        words=words.replace(c,"")
                words=words.lower()
                print(words)
                
fun()   

