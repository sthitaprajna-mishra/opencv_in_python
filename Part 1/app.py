import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image", image)
cv2.waitKey(0)

(h, w) = image.shape[:2]

# display image properties
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))

cv2.imwrite("photos/new_image.png", image)
