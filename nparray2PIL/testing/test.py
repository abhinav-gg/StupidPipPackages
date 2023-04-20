import PIL
import cv2
from nparray2pil import convert

image = cv2.imread("test.png")
pilimage = convert(image)
pilimage.show()