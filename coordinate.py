import cv2
import math
#import numpy as np

image = cv2.imread('/home/louxiantuo/picture/stone.jpg')
m = [[[0]*256]*256]*256
f = open('/home/louxiantuo/picture/allcoordinate.txt','a')

for x in range(0,image.shape[0]):
    for y in range(0,image.shape[1]):
        #countD = math.sqrt((standardB - image[x,y][0]) * (standardB - image[x,y][0]) + (standardG - image[x,y][1]) * (standardG - image[x,y][1]) + (standardR - image[x,y][2]) * (standardR - image[x,y][2]))
        #if countD < standardD :
            #print '[' + x + ',' + y + ']' + 'RGB' + '[' + image[x,y][0] + ',' + image[x,y][1] + ',' + image[x,y][2] + ']'
            #print("coordinate:[%d,%d],RGB:[%d,%d,%d]" % (x,y,image[x,y][0],image[x,y][1],image[x,y][2]))
            #count = count + 1
        m[image[x,y][2]][image[x,y][1]][image[x,y][0]] =  m[image[x,y][2]][image[x,y][1]][image[x,y][0]] + 1
        #f.writelines("\nRGB:[%d,%d,%d]" % (image[x,y][2],image[x,y][1],image[x,y][0]))

for i in range(256):
    for j in range(256):
        for k in range(256):        
            f.writelines("\nRGB:[%d,%d,%d],count = %d" % (i,j,k,m[i][j][k]))

f.close()