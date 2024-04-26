rows, cols = map(int, input().split())
colors_photo = []
for i in range(rows):
    row = list(map(str,input().split()))
    colors_photo.append(row)


''' 'C', 'M', 'Y', 'G', 'W' or 'B' '''

if 'C' in colors_photo or 'M' in colors_photo or 'Y' in colors_photo:
    print("#Color")
else:
    print("#Black&White")
