from img_process_lib import *


if __name__ == "__main__":
    imgP = imageProcessing()
    imgP.loadImage("yy.jpg")
    greyImg = imgP.getGreyimg()
    contouringImg = imgP.ContouringEuclidienneNorme(greyImg, 25)
    plt.imshow(contouringImg)
    plt.show()
    print(imgP.GausienFilter())
    # print(imgP.convolution(imgP.img, ([2,1],[2,1])))