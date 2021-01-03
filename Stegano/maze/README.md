#Maze

##Description
Santa is lost and can't deliver all the gifts ! Can you help him to get out !

###hint:
Santa is located at the blue point !

##Solution
We got a file `test.png` which is a 23px width and 23px height and with a blue dot in the middle.
IMAGE EHE
we read Exif data of the image
IMAGE HERE 
we found the following string in the Description 
`^[[A^[[A^[[A^[[C^[[C^[[A^[[D^[[D^[[D^[[D^[[A^[[A^[[A^[[A^[[D^[[A^[[A^[[C^[[A`
which is ANSI escape sequence for arrow keys 
if we convert them to directions it gives out the following :

-`^[[A`: Up
-`^[[B`: Down
-`^[[C`: Right 
-`^[[D`: Left

Now what's left is to follow the path and read each pixel value and convert it
and we get our flag ! 