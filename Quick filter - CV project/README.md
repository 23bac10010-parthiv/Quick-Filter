# Quick Filter - CV project

# Overview of Project

QuickFilter is a CLI based tool that will allow users to quickly apply computer vision filters to image directly from the terminal without need for heavy GUI apps.

## Features

- **Grayscale Conversion:** Converts RGB color images to black and white images.
- **Gaussian Blurring:** Softens image and removes noise
- **Edge detection:** Identifies and highlights object outlines in an image using Canny edge algorithm

## Technologies/Tools used

- Python 3
- OpenCV
- Argparse Library
- GitHub

## Steps to Install & Run the Project

1. Clone the repository.
2. Install Python 3.
3. Install the OpenCV library: 

```bash
pip install opencv-python
```

4. Place an image in the project folder.
5. Run the script using the following format:

```bash
python main.py --input <input_image_name> --ouput <output_image_name> --filter <filter_name>
```

## Instructions for Testing

Place a sample image named 'test.jpg' in the main project folder and run the following commands in your terminal one by one to verify each module:



**Test 1: Grayscale filter

```bash
python main.py --input test.jpg --output test_gray.jpg --filter gray
```


**Test 2: Blur filter

```bash
python main.py --input test.jpg --output test_blur.jpg --filter blur
```


**Test 3: Edge Detection filter

```bash
python main.py --input test.jpg --output test_edge.jpg --filter edge
```


**Test 4: Missing file error handling

```bash
python main.py --input missing_image.jpg --output error_test.jpg --filter gray
```


