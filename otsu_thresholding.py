#otsu's method assumes the image its being applied to is bi-modal,
#or that its histogram has 2 peaks
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_gray = cv2.GaussianBlur(gray, (7, 7), 0)

#apply otsu's thresholding method
T, thresh_inv = cv2.threshold(blurred_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Threshold", thresh_inv)
print(f"[INFO] otsu's thresholding value: {T}")

#display only the masker regions of the image
masked = cv2.bitwise_and(image, image, mask=thresh_inv)
cv2.imshow("Output", masked)
cv2.waitKey(0)