from util import *

for i in range(20,21):
	ds = dicom.read_file("./images_to_read/test_" + str(i) + ".dcm")
	img = ds.pixel_array # retrieve the image array

	nrows, ncols = img.shape
	sig = (nrows / 229.0, ncols / 187.0)
	# set the value of sigma according to the image's scale

	img = ndimage.gaussian_filter(img, sigma=sig, order=0, truncate=2.0)

	# plt.imshow(img, interpolation='nearest', cmap=pylab.cm.bone)
	# plt.savefig('./gaussian', bbox_inches='tight')

	global_thresh = threshold_otsu(img)
	th = global_thresh * 1.1
	binary_global = img > th # temp threshold

	# fig, axes = plt.subplots(nrows=3, figsize=(7, 8))
	# ax = axes.ravel()
	plt.gray()

	mask = binary_global > 0.8 * binary_global.mean()

	all_labels = measure.label(mask)
	blobs_labels, n_labels = measure.label(mask, background=0, return_num=True)

	sizes = ndimage.sum(mask, blobs_labels, range(n_labels + 1))

	# To find the leftmost, rightmost, upmost and downmost black pixel
	rows_z, cols_z = np.where(blobs_labels == 0)
	leftmost_z = cols_z.min()
	rightmost_z = cols_z.max()
	upmost_z = rows_z.min()
	downmost_z = rows_z.max()

	h,w = blobs_labels.shape
	blobs_labels[0:leftmost_z+1, rightmost_z-1:w] = 0
	blobs_labels[0:upmost_z+1, downmost_z-1:w] = 0

	if sizes.size > 1:
		temp = sizes.copy()
		temp.sort()
		minsize = temp[-2]

		mean_vals = ndimage.sum(img, blobs_labels, range(1, n_labels + 1))

		mask_size = sizes < minsize + 1
		remove_pixel = mask_size[blobs_labels]
		blobs_labels[remove_pixel] = 0


	# None-zeros
	# To find 
	rows, cols = np.nonzero(blobs_labels)
	leftmost = cols.min()
	rightmost = cols.max()
	upmost = rows.min()
	downmost = rows.max()

	width = rightmost - leftmost
	height = downmost - upmost

	w_z = rightmost_z - leftmost_z
	h_z = downmost_z - upmost_z

	rect = make_rect(leftmost, upmost, width, height)

	black_rect = make_rect(leftmost_z, upmost_z, w_z, h_z)


	save_image(blobs_labels, 
		'nipy_spectral', './out_images/img'+str(i)+'_cct', rect=rect)

	# save_image(ds.pixel_array, 
	# 	pylab.cm.bone, './final_images/img_final_' + str(i), rect=black_rect)


	#save_image(binary_global, None, './test_images/img' + str(i))

	# plt.imshow(binary_global)
	# plt.axis('off')


	#plt.savefig('./test_images/img')
	#plt.show()
		# j += 100

