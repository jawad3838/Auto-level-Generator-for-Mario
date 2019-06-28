from resizeimage import resizeimage
from PIL import Image,ImageDraw
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv
import os
import sys

path = "../level1specs/"
im_array = []
symbols_array = ["=","E","=","C","C","F","P","?","C","#","-","P","P","P","#","?","=","=","E","P","P","P","P","P","P","-"]

folder_levels = "../Edited/"
level_name = sys.argv[1]

orig_csv_save_path = "../levels_CSV/"
trans_csv_save_path = "../levels_transposed/"

ssim_array = []
max_val = 0
max_array = []
level=[]
w, h = 223, 13;
Matrix = [[0 for x in range(w)] for y in range(h)]
trans = [[0 for x in range(h)] for y in range(w)]


for i in range(1,27):
	name = path + str(i) + ".png"
	im_array.append(name)


def imgCompare(imageA):
		global ssim_array
		for i in range(0,len(im_array)):
		    M=Image.open(im_array[i])
		    match = resizeimage.resize_cover(M, [16, 16])
		    match.save(im_array[i])
		    xyz= resizeimage.resize_cover(imageA, [16, 16])
		    xyz.save("../level1specs/temp.png")
		    xyz=cv2.imread("../level1specs/temp.png")
		    match=cv2.imread(im_array[i])
		    match=cv2.cvtColor(match, cv2.COLOR_BGR2GRAY)
		    xyz=cv2.cvtColor(xyz, cv2.COLOR_BGR2GRAY)
		    ssim_ = measure.compare_ssim(xyz,match)
		    ssim_array.append(ssim_)

		max_val = max(ssim_array)			
		if(max_val < 0.5): max_array.append(11)
		else:
		 max_array.append(ssim_array.index(max(ssim_array))+1)
		ssim_array = []

def main():
        im = Image.open(folder_levels+level_name)
        count = 0
        for y in range (7,215,16):
                for x in range (16,3584,16):
                        if (x > 3584 or y > 215):
                                break;
                        img2 =im.crop((x,y ,x+16, y+16))
                        imgCompare(img2)
                        count += 1	 
                        #break
                #break
        #print count 
		
main()
print(max_array)
string = ""
f = open(orig_csv_save_path + os.path.splitext(level_name)[0] + ".csv", "w")
itr = 0
for i in range (0,13):
	for j in range (0,223):
		Matrix[i][j] = symbols_array[max_array[itr]-1]
		string += (symbols_array[max_array[itr]-1])
		itr += 1
	print(string)
	f.write(string)
	string = ""
	f.write("\n")
f.close()

r = open(trans_csv_save_path + os.path.splitext(level_name)[0] + "_trans.txt", "w")
temp = ""
for i in range(0, 223):
	for j in range(0, 13):
		trans[i][j] = Matrix[j][i]
		temp += trans[i][j]
	r.write(temp)
	temp = ""
	r.write("\n")
r.close()
#print trans
