# This python code will extract warm pixels(yellow to red) from the image and
# if a particular value is warm, the pixel is written into a text file else, '_' will be appended ('a')

# Importing Dependecies 
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image

# Defining a function to display image
def show_image(image):
    plt.figure(figsize = (5, 5))
    plt.imshow(image)
    plt.show()

# path to a specific Grad-CAM Superimposed Image
cam_img = Image.open("/Users/jahezabrahamjohny/Jahez/Research_CyberSecurity/ResearchPaperMaterial/grad_CAM[GS_Tr].jpeg")
# Converting the image into a numpy array
cam_img = np.array(cam_img)
show_image(cam_img)

# Creating a list of warm pixels
warm_pix = []
for i in range(256):
    for j in range(256):
        # If R > 120, G < 20 & B < 20 then it is Red warm. 
        # Red
        if cam_img[i,j,0] > 120 and cam_img[i, j, 1] < 20 and cam_img[i, j, 2] < 20:
            warm = list(cam_img[i,j])
            warm_pix.append(warm)
        # Orange and yellow
        elif cam_img[i,j,0] > 100 and cam_img[i,j,1] > 70 and cam_img[i,j,2] < 25:
            warm = list(cam_img[i,j])
            warm_pix.append(warm)
        # Dark red
        elif cam_img[i,j,0] > 50 and cam_img[i,j,1] < 10 and cam_img[i,j,2] < 20:
            warm = list(cam_img[i,j])
            warm_pix.append(warm)
print(warm_pix)

# Path and file name to store the warm pixels
file_name = 'Tracur'
path2 = '/Users/jahezabrahamjohny/Jahez/Research_CyberSecurity/Extract'

# Looping through every pixels of the 3 Channel image
for i in range(256):
    for j in range(256):
        pixel = list(cam_img[i,j])
        # Checking whether each pixel is warm
        if (pixel in warm_pix):
            count += 1
            # Appending the warm pixel to the list
            strr = np.array2string(cam_img[i,j])
            # Writing the pixel value to the txt file
            with open(r'{}/{}.txt'.format(path2, file_name), 'a') as fp:
                fp.write(strr)  # writing the valid opcode to the file
        else:
            # Appending '_' if the pixel is not warm
            with open(r'{}/{}.txt'.format(path2, file_name), 'a') as fp:
                fp.write('_')  # writing the valid opcode to the file
            # To count the number of warm pixels 

# To append the warm pixels
pix = []
for i in range(256):
    for j in range(256):
        pixel = list(cam_img[i,j])
        # Checking whether each pixel is warm
        if (pixel in warm_pix):
            count += 1
            # Appending the warm pixel to the list
            strr = np.array2string(cam_img[i,j])
            # Writing the pixel value to the txt file
            with open(r'{}/{}.txt'.format(path2, file_name), 'a') as fp:
                fp.write(strr)  # writing the valid opcode to the file
        else:
            # Appending '_' if the pixel is not warm
            with open(r'{}/{}.txt'.format(path2, file_name), 'a') as fp:
                fp.write('-')  # writing the valid opcode to the file
fp.close()

