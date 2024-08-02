import cv2
import numpy as np

# Load the image
image = cv2.imread("p1.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Get image dimensions
height, width, _ = image.shape

# Rotation
angle = 45
rotation_matrix = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Scaling
scale_factor = 0.5
scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

# Translation
x_translation, y_translation = 50, 50
translation_matrix = np.float32([[1, 0, x_translation], [0, 1, y_translation]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Scaled Image", scaled_image)
cv2.imshow("Translated Image", translated_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
