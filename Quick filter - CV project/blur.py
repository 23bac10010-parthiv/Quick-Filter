import cv2
def apply_blur(img):
    """Softens image using gaussian blur."""
    return cv2.GaussianBlur(img, (7, 7), 0)