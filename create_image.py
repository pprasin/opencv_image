import cv2
import numpy as np
import os

# image resolution details to be given below
height = 1080
width = 1920
file_path =  input("Enter the path to save the files : ")

for _ in range(256): #RGB Values are from 0 to 255
    blank_image = np.zeros((height,width,1),dtype="uint8")
    blank_image.fill(_) #Filling the image with a particular value - the value will range from 0 to 255
    file_name = os.path.join (file_path,"black_image_"+str(_)+".jpg")
    print ("the file name is {}".format(file_name))
    cv2.imwrite(file_name,blank_image) #writing the image to the desired location

