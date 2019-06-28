from PIL import Image,ImageDraw
import sys
import os

folder_path = "../Original_Levels/"
save_folder_path = "../Edited/"

level_name = sys.argv[1]

im = Image.open(folder_path + level_name)

maxX,maxY = im.size
X = 16
Y = 215
draw = ImageDraw.Draw(im)
while X <= maxX:
    draw.line((X, 0, X, maxY), fill = 255)
    X += 16

while Y >= 0:
    draw.line((0, Y, maxX, Y), fill=255)
    Y -= 16
del draw

im.save(save_folder_path + os.path.splitext(level_name)[0] + "-edited.gif")
#im = Image.open("Edited/edited-1.gif")
im.show()



