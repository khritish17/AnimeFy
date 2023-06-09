import cv2 as cv
from matplotlib import pyplot as plt
class AnimeFy:
    def __init__(self, fileName) -> None:
        self.fileName = fileName

        # image loaded in colour mode: 3 channel mode (BGR)
        self.original_image_BGR = cv.imread(filename = fileName, flags = 1)
        
        # image is read in gray scale
        self.grayScaleImage = cv.imread(fileName, 0)
        # self.display(self.grayScaleImage, mode = 0)

        # converting the color channel mode to RGB
        self.original_image_RGB = cv.cvtColor(self.original_image_BGR, cv.COLOR_BGR2RGB)
        # self.display(self.original_image_RGB, mode = 1)
        self.threshold(self.grayScaleImage)

    
    def threshold(self, imageSource):
        blurImage = cv.medianBlur(imageSource, 5)
        thresh = cv.adaptiveThreshold(blurImage, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        self.display(thresh)
        return thresh
    
    def display(self, imageMatrix, mode = 0):
        if mode == 0:
            cv.imshow('In-program display', imageMatrix)
            cv.waitKey(0)
            cv.destroyAllWindows()
        if mode == 1:
            plt.imshow(imageMatrix)
            plt.xticks([]), plt.yticks([])
            plt.show()


AF = AnimeFy('eye.png')