import cv2
import numpy as np

# Load the image
image = cv2.imread("p1.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Edge detection using Canny edge detector
edges = cv2.Canny(blurred_image, 50, 150)

# Texture extraction using Laplacian filter
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

# Display the original image and extracted features
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Laplacian Filter", laplacian)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
