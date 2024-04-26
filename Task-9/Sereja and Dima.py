n = int(input())
cards = list(map(int, input().split()))
 
Sereja = 0
Dima = 0
 
while cards:
    Sereja += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
    
    if not cards:
        break
        
    Dima += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
 
print(Sereja, Dima)




'''
import numpy as np
n = int(input())
cards = np.array(list(map(int, input().split())))
Sereja=0
Dima = 0

while(True):
    Sereja += max(cards[0],cards[-1])
    max_index = np.argmax([cards[0], cards[-1]])
    cards = np.delete(cards, max_index*-1)
    if cards.size <= 0:
        break
    Dima += max(cards[0],cards[-1])
    max_index = np.argmax([cards[0], cards[-1]])
    cards = np.delete(cards, max_index*-1)
    if cards.size <= 0:
        break

print(Sereja,Dima)
'''