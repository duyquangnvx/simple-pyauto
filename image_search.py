import cv2
from PIL import Image


# return top, left
def imageSearch(mainPath, subPath, accuracy = 0.9):
    grayImage = cv2.imread(mainPath, cv2.IMREAD_GRAYSCALE)
    #grayImage = cv2.cvtColor(mainImage, cv2.COLOR_BGR2GRAY)  
    template = cv2.imread(subPath, cv2.IMREAD_GRAYSCALE)

    result = cv2.matchTemplate(grayImage, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > accuracy:
        return max_loc
    else:
        return None