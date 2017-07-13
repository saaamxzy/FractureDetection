import matplotlib
matplotlib.use('Agg')

import dicom
from skimage import measure, filters
from skimage.filters import threshold_mean, threshold_otsu, threshold_local
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


import numpy as np
import scipy.ndimage as ndimage
import pylab


ds = dicom.read_file("test2.dcm")
img = ds.pixel_array # retrieve the image array
print(img.ndim)



nrows, ncols = img.shape
sig = (nrows / 229.0, ncols / 187.0)
# set the value of sigma according to the image's scale
print(sig)

img = ndimage.gaussian_filter(img, sigma=sig, order=0, truncate=2.0)


# plt.imshow(img, interpolation='nearest', cmap=pylab.cm.bone)
# plt.savefig('./gaussian', bbox_inches='tight')
# j = 4000

# while j < 14000:
image = img 
print(image.ndim)


global_thresh = threshold_otsu(image)
print('global threshold: ', global_thresh)
#8413
binary_global = image > global_thresh # temp threshold


fig, axes = plt.subplots(nrows=2, figsize=(7, 8))
ax = axes.ravel()
plt.gray()

ax[0].imshow(image)
ax[0].set_title('Original')

ax[1].imshow(binary_global)
ax[1].set_title('Global thresholding')
'''
ax[2].imshow(binary_adaptive)
ax[2].set_title('Adaptive thresholding')
'''
for a in ax:
	a.axis('off')

plt.savefig('./test_images/img', bbox_inches='tight')
#plt.show()
	# j += 100

