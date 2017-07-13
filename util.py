import matplotlib
matplotlib.use('Agg')

import dicom
from skimage import measure, filters
from skimage.filters import threshold_mean, threshold_otsu, threshold_local
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches


import numpy as np
from scipy import misc
import scipy.ndimage as ndimage
import pylab

def save_image(data, cm, fn, rect = None):
	sizes = np.shape(data)
	height = float(sizes[0])
	width = float(sizes[1])
	 
	fig = plt.figure()
	fig.set_size_inches(width/height, 1, forward=False)
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	fig.add_axes(ax)
	ax.imshow(data, cmap=cm)
	if rect != None:
		ax.add_patch(rect)

	plt.savefig(fn, dpi = height)
	plt.close()


def make_rect(x, y, width, height):
	rect = patches.Rectangle((x,y), 
		width, height, linewidth=1, edgecolor='r', facecolor='none')
	return rect
