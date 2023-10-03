import cv2 as cv
import numpy as np
class Assigner:
    def __init__(self, contours, hierarchy_root, image_matrix) -> None:
        self.contours = contours
        self.roots = hierarchy_root
        self.image = image_matrix
        height, width, color_mode = self.image.shape
        self.visited = [[0 for j in range(width)] for i in range(height)]
        self.output_image = np.zeros((height, width, color_mode), dtype=np.uint8)
        print(self.output_image.shape)
        print(self.image.shape)
        for root in self.roots:
            self.dfs(root)
        # cv.imshow('output', self.output_image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        # print(self.output_image.shape)
        # cv.imwrite('output.jpg', self.output_image)
        count = 0
        for i in range(height):
            for j in range(width):
                if self.visited[i][j] == 0:
                    count += 1
        print("{}/{}".format(count, height*width))

    
    def extreme_points(self, contour_id):
        # print("extreme point")
        cnt = self.contours[contour_id]
        leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
        rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
        topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
        bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
        points = [leftmost, rightmost, topmost, bottommost]
        # print(self.image.shape)
        # for point in points:
        #     cv.circle(self.image, point, 4, (0, 0, 255), -1)
        # cv.imshow('image', self.image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        return points

    def pixel_determination(self, contour_id, leftmost, rightmost, topmost, bottommost):
        # print("pixel_determination")
        left, right, top, bottom = leftmost[0], rightmost[0], topmost[1], bottommost[1]
        cnt = self.contours[contour_id]
        pixels = []
        # print("pixel: left:{}, right:{}, top:{}, bottom:{}".format(left, right, top, bottom))
        for x in range(left, right + 1):
            for y in range(top, bottom + 1):
                value = cv.pointPolygonTest(cnt,(x, y),False)
                # value: 1 -> inside the contour, -1 -> outside the contour, 0 -> on the contour
                if value == 1 or value == 0:
                    try:
                        if self.visited[x][y] == 0:
                            pixels.append((x, y))
                            self.visited[x][y] = 1
                    except:
                        print("Error at :({},{})".format(x, y))
                        # for the outer countour (the sqr one)
                        # there is no actual pixels assigned to it
                        # hence the visited will show key error, so ignore it
                        pass
        return pixels

    def color_processing(self, pixels):
        # print("color_processing")
        mean_blue = 0
        mean_green = 0
        mean_red = 0
        n = len(pixels)
        for x, y in pixels:
            mean_blue += self.image[x][y][0]
            mean_green += self.image[x][y][1]
            mean_red += self.image[x][y][2]
        mean_blue = mean_blue//n
        mean_green = mean_green//n
        mean_red = mean_red//n
        # print("B:{}, G:{}, R:{}".format(mean_blue, mean_green, mean_red))
        for x, y in pixels:
            self.output_image[x][y][0] = mean_blue
            self.output_image[x][y][1] = mean_green
            self.output_image[x][y][2] = mean_red
        

    def dfs(self, root):
        childrens = root.childrens
        for child in childrens:
            self.dfs(child)
        id = root.id
        leftmost, rightmost, topmost, bottommost = self.extreme_points(id)
        # print("id:{}, left:{}, right:{}, top:{}, bottom:{}".format(id, leftmost, rightmost, topmost, bottommost))
        pixels = self.pixel_determination(id, leftmost, rightmost, topmost, bottommost)
        # print(pixels)
        if pixels:
            # print(True)
            root.pixels = pixels
            self.color_processing(pixels)
        
        
