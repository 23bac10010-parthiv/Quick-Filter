import cv2

def apply_edge_detection(img):
    """Finds and highlights the edges of objects in the image."""
    # Conver to grayscale first for better edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Canny algorithm
    edges = cv2.Canny(gray, 100, 200)
    return edges
    