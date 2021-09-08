import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_gray = cv2.GaussianBlur(gray, (7, 7), 0)

#apply thresholding with a hardcoded value
T, thresh_inv = cv2.threshold(blurred_gray, 230, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Simple Thresholding", thresh_inv)
cv2.waitKey(0)

#apply Otsu's automatic thresholding
T, thresh_inv = cv2.threshold(blurred_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", thresh_inv)
cv2.waitKey(0)

#apply adaptive thresholding
thresh = cv2.adaptiveThreshold(blurred_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow("Mean Adaptive Thresholding", thresh)
cv2.waitKey(0)

#apply adaptive thresholding with a guassian weighting
thresh = cv2.adaptiveThreshold(blurred_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Guassian Adaptive Thresholding", thresh)
cv2.waitKey(0)
