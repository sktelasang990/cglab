import cv2

# Load the image
image = cv2.imread("p1.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Apply bilateral filter for smoothing
smoothed_image = cv2.bilateralFilter(image, 9, 75, 75)

# Display the original image and the processed images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Smoothed Image", smoothed_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
