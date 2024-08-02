import cv2

# Load the image
image = cv2.imread("p3.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Get image dimensions
height, width, _ = image.shape

# Split image into quadrants
left_quadrant = image[:, :width // 2]
right_quadrant = image[:, width // 2:]
top_quadrant = image[:height // 2, :]
bottom_quadrant = image[height // 2:, :]

# Display quadrants
cv2.imshow("Left Quadrant", left_quadrant)
cv2.imshow("Right Quadrant", right_quadrant)
cv2.imshow("Top Quadrant", top_quadrant)
cv2.imshow("Bottom Quadrant", bottom_quadrant)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
