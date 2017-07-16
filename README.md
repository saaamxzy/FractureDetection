# FractureDetection


## Limitations

During binarizations of the X-Ray images, a specific threshold is to be found for each dicom image, because the instruments used for imaging could vary thus resulting in different brightness, contrast or noises in each individual image. The method used here is called Otsu Threshold. However, given the effectiveness of Otsu's method on finding threshold in image binarization, the threshold found in this way is not guaranteed to be a perfect threshold to partition the pixel values into two values. The original .dcm files obtained from hospitals are partially defective because large portion of the image sources contain rather wide bright, white edges that are connected with the interested body parts of patients.

![image is coming soon]()

