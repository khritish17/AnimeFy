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
        # print(hierarchy)
        # print(contours[0])
        # for e in contours[0]:
        #     print(e, end="")
        # print(hierarchy[1])
        return contours

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
