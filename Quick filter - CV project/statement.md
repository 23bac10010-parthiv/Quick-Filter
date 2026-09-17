# Quick Filter - CV project

## Problem Statement

People often need to make simple edits to images like converting it to black and white or detect edges and using heavy software like Photoshop takes time and a lot of RAM. Also performing edits manually is repetitive and boring. Hence, there is a need for a lightweight, fast tool that can apply basic computer vision filters instantly and efficiently.

## Scope of the project

This project is a simple command line script built using pyton and OpenCV. The main focus is to apply basic image processing techniques without needing a graphical user interface.

The project will do the following

- Read normal images from the computer.
- Let user pick one of the three CV filters: Grayscale, Blur, or Edge Detection.
- Save the new edited image back to the computer.
- Run entirely in the terminal.
- Handl simple errors like telling the user if they typed the wrong image name instead of crashing.

## Target Users
- **Students:** Students who want to see a simple example of how basic OpenCV functions are put together in a real script.
- **Developers:** Programmers who need a quick script to preprocess some images before using them in other projects.

## High level Features

- **Command line Interface:** Uses python's `argparse` so the user can run the whole program by just typing the command in the terminal.
- **Grayscale Conversion:** Takes a standard color image and turns it into a simple black and white image.
- **Image blurring:** Uses a gaussian blur to soften the image and remove background noise.
- **Edge Detection:** Uses the Canny algorithm to find and highlight the outline of objects in the picture.
- **Safe file checking:** The scripts checks if the input file exists before trying to process it, which prevents the program from crashing.