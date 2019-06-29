import cv2
import math
#import numpy as np
import datetime

starttime =datetime.datetime.now()

image_path = '/home/louxiantuo/picture/626-1/14-1-r.jpg'
result_txt_path = '/home/louxiantuo/picture/626-1/result/14-1-r.txt'
result_jpg_path = '/home/louxiantuo/picture/626-1/result/14-1-r.jpg'

image = cv2.imread(image_path)

f = open(result_txt_path,'a')
#standardRGB
standardB = 49
standardG = 39
standardR = 150
#standardD
standardD = 200
MatWhite = image
#count %
count = 0
count_white = 0
for x in range(0,image.shape[0]):
    for y in range(0,image.shape[1]):
        countD = math.sqrt((standardB - image[x,y][0]) * (standardB - image[x,y][0]) + (standardG - image[x,y][1]) * (standardG - image[x,y][1]) + (standardR - image[x,y][2]) * (standardR - image[x,y][2]))
        if image[x,y][0] == 255 and image[x,y][1] == 255 and image[x,y][2] == 255:
            count_white = count_white + 1
        elif countD < standardD :
            #print '[' + x + ',' + y + ']' + 'RGB' + '[' + image[x,y][0] + ',' + image[x,y][1] + ',' + image[x,y][2] + ']'
            print("coordinate:[%d,%d],RGB:[%d,%d,%d]" % (x,y,image[x,y][0],image[x,y][1],image[x,y][2]))
            count = count + 1
            #f.writelines("\ncoordinate:[%d,%d],RGB:[%d,%d,%d]" % (x,y,image[x,y][2],image[x,y][1],image[x,y][0]))
            f.writelines("\n[%d,%d,%d]," % (image[x,y][2],image[x,y][1],image[x,y][0]))
        else:
            MatWhite[x,y][0] = 255
            MatWhite[x,y][1] = 255
            MatWhite[x,y][2] = 255

print count
print count_white
print image.shape[0] * image.shape[1]   
f.writelines("\nSumPointCount:%d" % (count))
f.writelines("\nWhitePointCount:%d" % (count_white))
f.writelines("\nStonePointCount:%d" % (image.shape[0] * image.shape[1] - count_white))
f.writelines("\nImage height: %d" %(image.shape[0]))
f.writelines("\nImage width:%d" % (image.shape[1]))
f.writelines("\nImage height * width:%d" % (image.shape[0] * image.shape[1]))
f.close()


cv2.imwrite(result_jpg_path,MatWhite)

endtime = datetime.datetime.now()

print (endtime - starttime).seconds