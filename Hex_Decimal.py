# Importing necessary packages
import os.path
from os import listdir
import numpy as np
import math

# Path to input and output file
path = "/media/research/TOSHIBA EXT/Big2015/hex_code"            #input file’s path
path2 = "/media/research/TOSHIBA EXT/Big2015/hex_dec"      #output file’s path
    

for i in (listdir(path)):                     #OPENING A PARTICULAR CLASS
    class_name = os.path.basename(os.path.join(path,i)) 
    print(class_name)
    path3 = path+"/"+i  #path of particular file in each clss
    
    for j in(listdir(path3)):
        output_stream = ""
        contents = open(os.path.join(path3,j),"r",errors='ignore')   #opening a particular opcode file of an exe
        file_name = os.path.basename(os.path.join(path3,j)) #storing file name
        print(file_name)
        for lis in contents:
          hex_list = lis
          #hex_list = ' '.join(hex_list).split()
          hex_list = hex_list.replace('\n', '').split(" ")
          #print(data_list)
          table = {'0': 0, '1': 1, '2': 2, '3': 3,
          '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'A': 10, 'B': 11,
          'C': 12, 'D': 13, 'E': 14, 'F': 15}
          dec_list = []
          for ele in hex_list:
            hexadecimal = ele.strip().upper()
            res = 0
            size = len(hexadecimal) - 1
            for num in hexadecimal:
              res = res + table[num]*16**size
              size = size - 1
            dec_list.append(res)
            #print(dec_list)
