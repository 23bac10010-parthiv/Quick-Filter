import argparse
import sys
from file_handler import read_image, save_image
from grayscale import apply_grayscale
from blur import apply_blur
from edge import apply_edge_detection

def main():
    # setup terminal commands
    parser =  argparse.ArgumentParser(description="Quickfilter")
    parser.add_argument('--input',required=True, help="Input image file name")
    parser.add_argument('--output',required=True, help="Output image file name")
    parser.add_argument('--filter',required=True, choices=['gray', 'blur', 'edge'], help="choose filter")

    args = parser.parse_args()

    # Read the image
    print (f"Loading {args.input}...")
    img = read_image(args.input)

    if img is None:
        sys.exit(1) # stops program if image isn't found

    # Apply chosen filter
    print(f"Applying '{args.filter}' filter...")
    if args.filter == 'gray' :
        result = apply_grayscale(img)
    elif args.filter == 'blur' :
        result = apply_blur(img)
    elif args.filter == 'edge' :
        result = apply_edge_detection(img)

    save_image(args.output, result)

if __name__ == "__main__" :
    main()