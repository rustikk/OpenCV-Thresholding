#3 types of thresholding: simple, Otsu and adaptive thresholding
#simple thresholding you manually supply the parameters
#otsu's thresholding automatically compute the optimal threshold value based
#on the input image.
#adaptive thresholding breaks the image down into smaller pieces and thresholds
#each of the pieces seperately.
"""
Thresholding is the binarization of an image. In general, we seek to convert a
grayscale image to a binary image, where the pixels are either 0 or 255.

A simple thresholding example would be selecting a threshold value T, and then
setting all pixel intensities less than T to 0, and all pixel values greater
than T to 255. In this way, we are able to create a binary representation of
the image.
"""
#thresholding is able to extract objects out of an image from
#the objects background
import argparse
import cv2

#build the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to input img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#apply a 7x7 guassian blur
blurred_gray = cv2.GaussianBlur(gray, (7, 7), 0)

#basic thresholding
#the threshold_check number is the value used to to threshold.
#if a pixel is greater that pixel is set to black, if its under the threshold check
#then that pixel is set to white
#cv2.threshold(image_to_thresh, threshold_check(int), output_value_for_thresholding, cv2.THRESHOLDING_METHOD)
T, thresh_inv = cv2.threshold(blurred_gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", thresh_inv)

#normal thresholding
T, thresh = cv2.threshold(blurred_gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholding Binary", thresh)

#show the masked regions of the image
masked = cv2.bitwise_and(image, image, mask=thresh_inv)
cv2.imshow("Output", masked)
cv2.waitKey(0)