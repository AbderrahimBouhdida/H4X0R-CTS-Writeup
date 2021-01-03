import numpy as np
from PIL import Image

directions = "^[[A^[[A^[[A^[[C^[[C^[[A^[[D^[[D^[[D^[[D^[[A^[[A^[[A^[[A^[[D^[[A^[[A^[[C^[[A"

img = Image.open("test.png")

data = np.asarray( img, int )

print(data.shape)

path = directions.split('^[[')

print(path)
x = 11
y = 11

flag = "" 
for step in path:
	if step == 'A':
		y = y - 1 
		flag+=chr(data[x][y][0])
	if step == 'C':
		x = x + 1
		flag+=chr(data[x][y][0])
	if step == 'D':
		x = x - 1 
		flag+=chr(data[x][y][0])

print(flag)