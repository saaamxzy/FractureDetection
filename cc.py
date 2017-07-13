from util import *


#ds = dicom.read_file("test2.dcm")
img = misc.imread('img.png', mode='L') # retrieve the image array

# img = ndimage.gaussian_filter(img, sigma=sig, order=0, truncate=2.0)


# plt.imshow(img, interpolation='nearest', cmap=pylab.cm.bone)
# plt.savefig('./gaussian', bbox_inches='tight')

mask = img > 0.8 * img.mean()

all_labels = measure.label(mask)
blobs_labels, n_labels = measure.label(mask, background=0, return_num=True)

sizes = ndimage.sum(mask, blobs_labels, range(n_labels + 1))

if sizes.size > 1:
	temp = sizes.copy()
	temp.sort()
	minsize = temp[-2]

	mean_vals = ndimage.sum(img, blobs_labels, range(1, n_labels + 1))

	mask_size = sizes < minsize + 1
	remove_pixel = mask_size[blobs_labels]
	blobs_labels[remove_pixel] = 0
print blobs_labels.shape

rows, cols = np.nonzero(blobs_labels)
leftmost = cols.min()
rightmost = cols.max()
upmost = rows.min()
downmost = rows.max()

width = rightmost - leftmost
height = downmost - upmost

rect = make_rect(leftmost, upmost, width, height)

ds = dicom.read_file("test2.dcm")
img = ds.pixel_array # retrieve the image array

save_image(img, 
	pylab.cm.bone, './test_images/img_final', rect=rect)



# plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
# plt.axis('off')
# plt.imshow(blobs_labels, cmap='nipy_spectral')


# plt.savefig('./test_images/img_cc', bbox_inches=0)


#plt.show()
