import cv2
import numpy as np

# Load image
image = cv2.imread("document.jpg")
orig = image.copy()

# Resize for easier processing
ratio = image.shape[0] / 500.0
image = cv2.resize(image, (int(image.shape[1] / ratio), 500))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur + edge detection
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blur, 75, 200)

# Find contours
contours, _ = cv2.findContours(
    edged.copy(),
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

doc = None

# Find 4-point contour
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        doc = approx
        break

# Draw contour
cv2.drawContours(image, [doc], -1, (0, 255, 0), 2)

# Show result
cv2.imshow("Detected Document", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
