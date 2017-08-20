# FractureDetection
## Introduction
This program aims to propose a region of interest for radiologic diagnosis. To be more specific, for each input X-Ray image, it outputs a image with a region highlighted. That region is supposed to suggest useful region of an X-Ray(part that shows bone structures). This could be useful for deep learning purposes specialized in fracture detection networks.
## Required Environment
Python 2.7
Python packages:
  pydicom, skimage, matplotlib, numpy, scipy, pylab

## Instructions
current directory = directory where the scripts are

1. Put all patients' folders to be processed in a file called Images in the current directory.
2. Run extract_image.py to extract all .dcm files from all the patients' folders.
3. Run save_image.py to process all .dcm files.

note:
  - images_to_read stores all images in .dcm format
  - test_images stores all binary images
  - out_images stores all gray scale images with rectangles drawn
  - final_images stores all marked images
  - original_images stores all .dcm files in cmap pylab.cm.bones

## Limitations

During binarizations of the X-Ray images, a specific threshold is to be found for each dicom image, because the instruments used for imaging could vary thus resulting in different brightness, contrast or noises in each individual image. The method used here is called Otsu Threshold. However, given the effectiveness of Otsu's method on finding threshold in image binarization, the threshold found in this way is not guaranteed to be a perfect threshold to partition the pixel values into two values. The original .dcm files obtained from hospitals are partially defective because large portion of the image sources contain rather wide bright, white edges that are connected with the interested body parts of patients.

<img src="./white_border.png" width="200">
White borders on both sides of the image

To avoid this issue as much as possible, we made an assumption: in most cases, the brightness of the body parts will be of higher value(value of pixel in grayscale, 0 is black, 255 is white and thus brightest) than those unwanted white edges.
