a=input("enter the string:")
wordlist=a.split()
b=[]
for i in wordlist:
    b.append(i.capitalize())
print(" ".join(b))
