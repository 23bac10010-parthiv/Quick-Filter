import cv2
def apply_grayscale(img):
    """Converts color image to black and white."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)