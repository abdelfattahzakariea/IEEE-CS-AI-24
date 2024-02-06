sentence=input("enter the sentence : ")
sentence = sentence.split() #=> The split() method splits a string into alist.
#print (len(sentence))

reverses =""
for x in reversed(range(0,len(sentence))):
    reverses +=(sentence[x]+" ")

print(reverses)

#print(sentence.replace(sentence[0:sentence.find(" ")] , sentence[sentence.rfind(" "):len(sentence)])) 
