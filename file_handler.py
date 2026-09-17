import cv2
import os

def read_image(filename):
    """Loads an image and checks if the file actually exists."""
    if not os.path.exists(filename):
        print(f"The file '{filename}' was not found in the folder.")
        return None
    return cv2.imread(filename)

def save_image(filename, img_data):
    """Saves the edited image."""
    cv2.imwrite(filename,img_data)
    print(f"Edited image saved as '{filename}'")