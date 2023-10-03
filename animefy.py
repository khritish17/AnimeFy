import cv2 as cv

class Animefy:
    def __init__(self) -> None:
        self.image_matrix = None
        self.color_image = None
    
    def getContours(self):
        thresh = self.threshold()
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        # cv.drawContours(self.color_image, contours, -1, (255, 0, 0), 1)
        # display(self.color_image)

        # color = [(0, 0, 255), (102, 255, 102), (255, 0, 0), (0, 255, 255), (255, 255, 102), (152, 51, 255), (51, 51, 153)]
        # for i in range(len(contours)):
        #     temp = self.color_image
        #     cv.drawContours(temp, contours, i, color[i], 3)
        #     display(temp)

        # print(hierarchy)
        # print(contours[0])
        # for e in contours[0]:
        #     print(e, end="")
        # print(hierarchy[1])
        return contours, hierarchy

    def threshold(self):
        blur = cv.medianBlur(self.image_matrix, 5)
        thresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        return thresh

    def load_image(self, raw_image):
        
        # load the image to the memory
        try:
            self.color_image = cv.imread(raw_image)
            self.image_matrix = cv.imread(raw_image, 0)
            # cv.imshow('{}'.format(raw_image), self.image_matrix)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            return self.color_image
        except:
            print("No image found, check again!!")

# Anime = Animefy() 
# Anime.load_image('1.jpg')
def display(image):
    try:
        # img = cv.imread(image)
        cv.imshow('{}'.format(image), image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except:
        print("No image found, check again")
