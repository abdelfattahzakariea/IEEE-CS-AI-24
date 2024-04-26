rows, cols = map(int, input().split())
colors_photo = []
for i in range(rows):
    row = list(map(str,input().split()))
    colors_photo.append(row)
''' 'C', 'M', 'Y', 'G', 'W' or 'B' '''

colors_photo_flat = [color for sublist in colors_photo for color in sublist] # comprahinsive style 

if 'C' in colors_photo_flat or 'M' in colors_photo_flat or 'Y' in colors_photo_flat:
    print("#Color")
else:
    print("#Black&White")




'''
import numpy as np 
 
rows, cols = map(int, input().split())
colors_photo = []
for i in range(rows):
    row = list(map(str,input().split()))
    colors_photo.append(row)
 
arr = np.array(colors_photo)
 
''' 'C', 'M', 'Y', 'G', 'W' or 'B' '''
 
if np.any((arr == 'C') | (arr == 'M') | (arr == 'Y')):
    print("#Color")
else:
    print("#Black&White")
'''