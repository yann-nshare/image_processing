##
# yann.nshare@epitech.eu PROJECT, 2019
# my_project
# File description:
# use_img_lib.py
##


# importation des librairies
from numpy import sqrt
import matplotlib.pyplot as plt
import sys
import numpy as np
from PIL import Image,ImageFilter


# objet for apply a masque or filter

class imageProcessing():
    def __init__(self, path=None):
      self.ImageFile = None
      self.img = None

    # load image and exit 1 if path not found
    def loadImage(self, path=None):
        self.ImageFile = path
        try:
            self.img = Image.open(self.ImageFile)
        except IOError:
            print('Error opening imageFile' + self.ImageFile)
            exit(1)

    def getGreyimg(self):
        if self.img == None:
            print("img object not load")
            exit(1)
        colonne,ligne = self.img.size
        imgC = Image.new(self.img.mode,self.img.size)
        for i in range(ligne):
            for j in range(colonne):
                pixel = self.img.getpixel((j,i)) # get pixel
                # calcul du poids de chaque composante du gris dans le pixel (CIE709)
                gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] +  0.0721 * pixel[2])
                # en gris les 3 composantes RGB sont identiques
                p = (gris,gris,gris)
                # composition de la nouvelle image 
                imgC.putpixel((j,i), p)
        return imgC

    # get contoure of image with greylevel (greyscale)
    # warning after that, imgage needs to be shades of grey
    def ContouringEuclidienneNorme(self, img=None, seuil=30):
        if img == None:
            print("img object not load")
            exit(1)
        colonne,ligne = img.size
        imgC = Image.new(img.mode,img.size)
        for i in range(1,ligne-1):
            for j in range(1,colonne-1):
                p1 = img.getpixel((j-1,i))
                p2 = img.getpixel((j,i-1))
                p3 = img.getpixel((j+1,i))
                p4 = img.getpixel((j,i+1))
                n = self.EuclidienneNorme(p1,p2,p3,p4)
                if n < seuil:
                    imgC.putpixel((j - 1, i - 1), (255, 255, 255))
                else:
                    imgC.putpixel((j - 1, i -1), (0, 0, 0))
        return imgC

    def EuclidienneNorme(self, p1,p2,p3,p4):
        return sqrt((p1[0]-p3[0])*(p1[0]-p3[0]) + (p2[0]-p4[0])*(p2[0]-p4[0])) # calcul of gradient
    
    # in progress
    def convolution(self, img, filter, mode=0):
        imgC = Image.new("RGB", (int(img.size[0]/len(filter[0])), int(img.size[1]/len(filter))))
        result = 0
        mat = 2*[2*[]]
        img = ([3,3],[3,3])
        for y in range(len(filter)):
            for h in range(len(filter[0])):
                for x in range(len(filter[0])):
                    # result += img.getpixel((y,x))[0] * filter[x][h]
                    result += img[y][x] * filter[x][h]
                # imgC.putpixel((
                # y, h), ) = result
                mat[y].append(result)
                result = 0
            # mat[y][h] = resultresult += img.getpixel((y,x))[0] * filter[x][h]
        return mat
    
    def GausienFilter(self, shape=(3,3),sigma=0.5): #for 2d
        """
        2D gaussian mask - should give the same result as MATLAB's
        fspecial('gaussian',[shape],[sigma])
        """
        m,n = [(ss-1.)/2. for ss in shape]
        y,x = np.ogrid[-m:m+1,-n:n+1]
        h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
        h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
        sumh = h.sum()
        if sumh != 0:
            h /= sumh
        return h
