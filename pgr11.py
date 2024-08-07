import cv2
image = cv2.imread("p3.jpg")
if image is None:
    print("Error: Unable to load image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Threshold the image to create a binary image
_, threshold_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the original image and the contour image
cv2.imshow("Original Image", image)
cv2.imshow("Contour Image", contour_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
