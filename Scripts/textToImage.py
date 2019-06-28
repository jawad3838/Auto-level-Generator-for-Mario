from PIL import Image,ImageDraw
import sys
import os

size = 3364,216
text = ""
w, h = 213, 13;
copy = 0
newImage = Image.new("RGBA", size, "white")
path = "../level1specs/"
newLevelPath = '../Generated_levels/'

pictures = []
symbols_array = ["=","e","=","c","c","f","p","?","c","#","-","p","p","p","#","?","=","=","e","p","p","p","p","p","p","-"]

trans = [[0 for x in range(w)] for y in range(h)]

def convertToImage(filename_complete_path, filename):

        global copy
        r = open(filename_complete_path, "r")

        for i in range(0, 13):
                text= r.readline()
                for c in text:
                        if(copy == 213): break
                        if(c == '\n'): continue
                        trans[i][copy] = c
                        copy += 1
                text = ""
                copy = 0
        r.close()

        print(trans)

        for i in range(0,13):
        	for j in range(0,213):
        		pictures.append(symbols_array.index(trans[i][j])+1)

        itr = 0
        for y in range (7,213,16):
        	for x in range (16,3416,16):
        		if (x > 3408 or y > 213): break;
        		imgPath = path+str(pictures[itr])+".png"
        		img = Image.open(imgPath)
        		newImage.paste(img,(x,y))
        		itr += 1
        print(itr)
        newImage.save(newLevelPath+os.path.splitext(filename)[0]+'.png')
