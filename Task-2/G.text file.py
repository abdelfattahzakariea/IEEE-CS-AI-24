import os

count_of_words={}

with open("C:\\Users\\abdel\\OneDrive\\Desktop\\python\\Sample.txt","r") as file:
    text=""+file.read()
    print(text)
    text=text.split()

for key in text:
        count_of_words[key]=text.count(key)
for key ,value in count_of_words.items():
    print(f"the word ' {key} ' occurence => {value}")