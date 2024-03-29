# Malware exe --> HexCode (HexEditor)
# HexCode (HexEditor) --> Hexadecimal
# Hexadecimal (Python) --> Decimal (Refer to Hex_Decimal.py)
# Decimal (Python) --> Grayscale Image

# Connecting to Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Importing necessary packages 
import os.path
from os import listdir
import numpy as np
import imageio
import math
from PIL import Image as im
from numpy import *

# Setting the path to input and output folder
path = "/content/drive/MyDrive/Malware Analysis/hex_dec"  # input file’s path
path2 = "/content/drive/MyDrive/Malware Analysis/dec_img"  # output file’s path

count = 0
for i in (listdir(path)):  # OPENING A PARTICULAR CLASS
    class_name = os.path.basename(os.path.join(path, i))
    path3 = path + "/" + i  # path of particular file in each clss
    print(class_name)
    for j in (listdir(path3)):
        array_mat = np.zeros((62, 62))  # 62x62 metrix
        myfile = open(os.path.join(path3, j), "r", errors='ignore')  # opening a particular opcode file of an exe
        file_name = os.path.basename(os.path.join(path3, j))
        contents = myfile.read()
        str_list = contents.replace('\n', '').split(" ") # Eliminating spaces
        str_list = contents.replace(',', '').split(" ") # Eliminating , 
        dec_list = []
        for ele in str_list:
          dec_list.append(ele)
        
        # changing list to an array
        dec_arr = np.array(dec_list)
        
        # 256 x 256 matrix
        array_mat = np.zeros((256, 256))

        # stripping ] from the last element
        temp = dec_arr[len(dec_arr)-1]
        fir = temp[-1]
        strr1 = temp.rstrip(fir)
        dec_arr[len(dec_arr)-1] = strr1


        # stripping [ from the first element
        for i in range(0, len(dec_arr)-1):
          if i == 0:
            strr = str(dec_arr[i])
            fir = strr[0]
            strr1 = strr.lstrip(fir)
            dec_arr[i] = strr1
            #print(type(dec_arr[i]))
            #print(strr1)
        
        # indexing
        for i in range(0,len(dec_arr)-1):
          ele1 = dec_arr[i]
          n = i+1
          ele2 = dec_arr[n]
          i+=1
          ele1 = int(ele1)
          ele2 = int(ele2)
          array_mat[ele1][ele2] += 1
        
        # ceiling the array elements
        rows = len(array_mat);  
        cols = len(array_mat[0]);
        for i in range(0, rows):
          sumRow = 0;
          for j in range(0, cols):
            sumRow = sumRow + array_mat[i][j];
            array_mat[i][j] = np.ceil((array_mat[i][j]/sumRow)*256)
        
        array_mat = np.array(array_mat)
        
        # converting the array into image and storing it into data
        data = im.fromarray(array_mat)

        # converting the image into RGB mode
        if data.mode != 'RGB':
          data = data.convert('RGB')
        
        path4 = path2 + "/" + class_name  # saving path with classname
        # saving the image into target file
        print('Saving image from {}'.format(file_name))
        imageio.imwrite('{}/{}.png'.format(path4, file_name), data)
        count += 1
        print(count)
